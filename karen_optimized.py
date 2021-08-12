import datetime
import tkinter
import threading
import pyttsx3
import requests
import speech_recognition as sr
import winsound
import logging
import skills
import utils.vosk_listen as vosk
import database
from utils import controller
from utils.settings import MyConfiguration
from utils.autocomplete3 import AutocompleteEntry

commands_list = skills.get_all_commands()
DEFAULT_TEXT = "Hi! What can i help you with?"

# logging.basicConfig(filename="karenlog.log",
#                     format='%(asctime)s %(message)s',
#                     filemode='w')
# logger = logging.getLogger("karen")
# logger.setLevel(logging.DEBUG)
# logger.debug("Logging debug started!")

listen_thread = None
process_thread = None
reset_thread = None

# wake_word_thread = None
# start_thread = None

wake_word_sound = "sounds/wakeup_sound.wav"
thinking_sound = "sounds/thinking.wav"
stop_listen_sound = "sounds/stop_listening.wav"


def on_click_mic():
    global listen_thread
    if listen_thread is not None and listen_thread.is_alive():
        pass
    else:
        listen_thread = threading.Thread(target=listen_process_thread)
        listen_thread.setDaemon(True)
        listen_thread.start()

    # logger.debug("Mic button clicked!")
    # logger.debug("Starting listening_process thread...")
    # logger.debug("listening_process thread started!")


def on_click_entry(event):
    global process_thread
    # logger.debug("Text entered!")
    text = input_entry.get()
    input_entry.delete(0, tkinter.END)
    if text == "":
        return
    # logger.debug("Starting process thread...")
    if process_thread is not None and process_thread.is_alive():
        pass
    else:
        process_thread = threading.Thread(target=process, args=(text,))
        process_thread.setDaemon(True)
        process_thread.start()
    # logger.debug("process thread started!")


def print_output(text):
    # logger.debug("Printing output: {}...".format(text))
    print(text)
    output_text.config(text=text)
    # logger.debug("Output printed: {}!".format(text))


# Initializing pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


def start():
    config = MyConfiguration()
    username = config.username
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning\n{}!".format(username))
    elif 12 <= hour < 18:
        speak("Good Afternoon\n{}!".format(username))
    else:
        speak("Good Evening\n{}!".format(username))


def check_internet():
    # logger.debug("Checking internet connection...")
    url = "http://www.google.com"
    timeout = 2
    try:
        requests.get(url, timeout=timeout)
        # logger.debug("Internet is connected!")
        return True
    # except (requests.ConnectionError, requests.Timeout) as exception:
    except Exception as e:
        # logger.debug("Internet is disconnected!")
        print(e)
        return False


def speak(text):
    global reset_thread
    # logger.debug("Speaking: {}...".format(text))
    if engine._inLoop:
        print("Engine is in loop!")
        engine.endLoop()
    print_output(text)
    engine.say(text)
    engine.runAndWait()
    # logger.debug("Speaking: {} finished!".format(text))
    if reset_thread is not None and reset_thread.is_alive():
        reset_thread.cancel()
    else:
        reset_thread = threading.Timer(30.0, reset_output)
        reset_thread.start()


def reset_output():
    print_output("Hi! How can i help you?")


def start_listen_process_thread():
    pass


def listen_process_thread():
    # logger.debug("listening_process thread called!")
    text = listen()
    input_entry.insert(0, text)
    input_entry.selection_range(0, tkinter.END)
    process(text)
    # logger.debug("Exiting listening_process thread!")


def listen_vosk():
    # logger.debug("Vosk: Listening...")
    mic_button.config(bg="red")
    text = vosk.listen()
    play_sound(stop_listen_sound)
    mic_button.config(bg="white")
    # logger.debug("Vosk: Listened: {}".format(text))
    return text


def listen_google():
    # logger.debug("Google: Listening...")
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            mic_button.config(bg="green")
            r.energy_threshold = 4000
            audio = r.listen(source)
            mic_button.config(bg="white")
        said = ""
        try:
            play_sound(thinking_sound)
            print_output("Recognizing...")
            said = r.recognize_google(audio)
            print_output(said)
        except sr.UnknownValueError as e:
            speak("Sorry, I didn't hear anything! Please try again!")
            # logger.error(e)
        except sr.RequestError as e:
            speak("You don't have internet connection! Try enabling the speech_rec to 'both' or 'vosk'.!")
            # logger.error(e)
        play_sound(stop_listen_sound)
        # logger.debug("Google: Listened: {}!".format(said))
        return said.lower()
    except sr.WaitTimeoutError as e:
        play_sound(stop_listen_sound)
        speak("Sorry, I didn't hear anything! Please try again!")
    except OSError as e:
        speak("Please check your microphone!")
        # logger.error(e)


def listen():
    # logger.debug("Listening...")
    config = MyConfiguration()
    speech_rec = config.speech_rec
    print_output("Listening...")
    play_sound(wake_word_sound)
    if speech_rec == "both":
        if check_internet():
            return listen_google()
        else:
            return listen_vosk()
    elif speech_rec == "google":
        return listen_google()
    elif speech_rec == "vosk":
        return listen_vosk()
    else:
        print_output("No STT engine found: {}".format(speech_rec))


def process(text):
    # logger.debug("Processing: {}".format(text))
    mic_button.config(bg="white")
    if text is None or text == "":
        return
    response = skills.execute(text)
    if response:
        speak(response)
    else:
        speak("Sorry, I didn't understand! Please try again!")
    command = database.CommandDatabase()
    command.add_command(text, response, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))


def listen_wake_word():
    config = MyConfiguration()
    wake_word = config.wake_word
    # logger.debug("Listening for wake_word: {}".format(WAKE_WORD))
    while True:
        print("Listening for wake_word...")
        word = vosk.listen_wake_word()
        if wake_word in word:
            # logger.debug("wake word detected!")
            listen_process_thread()


# Getting configuration settings
# if os.path.exists("utils/config.ini"):
#     try:
#         config = configparser.ConfigParser()
#         config.read('utils/config.ini')
#         settings = dict(config.items('SETTINGS'))
#         api_keys = dict(config.items('API_KEYS'))
#
#         first_time = settings["first_time"]
#         ASSISTANT_NAME = settings["assistant_name"]
#         USERNAME = settings["username"]
#         speech_rec = settings["speech_rec"]
#         WAKE_WORD = settings["wake_word"]
#         NEWSAPI = api_keys['news_api']
#
#         s = json.dumps(settings, sort_keys=True, indent=4)
#         a = json.dumps(api_keys, sort_keys=True, indent=4)
#
#         # logger.debug("Configurations loaded: \n{}\n{}".format(s, a))
#     except configparser.Error:
#         print("Error Reading config.ini")


def play_sound(path):
    winsound.PlaySound(path, winsound.SND_ASYNC | winsound.SND_ALIAS)


# config = MyConfiguration()
#
# first_time = config.first_time
# wake_word = config.wake_word
# assistant_name = config.assistant_name
# speech_rec = config.speech_rec
# username = config.username


main_window = tkinter.Tk()
mic_img = tkinter.PhotoImage(file="images/mic.png")
mic_image = mic_img.subsample(10, 10)
main_window.title("Karen")
main_window.geometry("320x480-8+60")

main_frame = tkinter.Frame(main_window, border=1, background='green')
main_frame.pack(fill="both", expand=True)
bottom_frame = tkinter.Frame(main_window)
bottom_frame.pack(side="bottom", anchor="w", fill="x")

output_text = tkinter.Label(main_frame)
output_text.config(font=("Calibri", 12, "bold"), wraplength="250")
output_text.pack(fill="both", expand=True)
# controller.set_output_text(output_text)

input_entry = AutocompleteEntry(bottom_frame, width="34")
input_entry.set_completion_list(commands_list)
input_entry.config(font="Calibri, 11")
input_entry.pack(side="left", ipady=7)
input_entry.focus_set()

# input_entry = tkinter.Entry(bottom_frame, width="34")
# input_entry.config(font="Calibri, 11")
# input_entry.pack(side="left", ipady=7)

mic_button = tkinter.Button(bottom_frame, image=mic_image, width="50", height="30", relief="flat", command=on_click_mic)
mic_button.pack(side="right")

# input_entry.focus()
input_entry.bind('<Return>', on_click_entry)

wake_word_thread = threading.Thread(target=listen_wake_word)
wake_word_thread.setDaemon(True)

start_thread = threading.Thread(target=start)
start_thread.setDaemon(True)


def start_threads():
    start_thread.start()
    wake_word_thread.start()


controller.speak = speak
controller.listen = listen
controller.play_sound = play_sound

main_window.after(1000, start_threads)
main_window.mainloop()
