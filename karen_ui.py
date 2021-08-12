import datetime
import tkinter
import threading
import os
import subprocess
import time
import pyttsx3
import wikipedia
import speech_recognition as sr
import utils.vosk_listen as vosk
from playsound import playsound
import speedtest
import requests
import webbrowser
import configparser
import pandas as pd
import pyjokes
import logging
import json

DEFAULT_TEXT = "Hi! What can i help you with?"

logging.basicConfig(filename="karenlog.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger("karen")
logger.setLevel(logging.DEBUG)
logger.debug("Logging debug started!")


def on_click_mic():
    logger.debug("Mic button clicked!")
    start_listen_thread()


def on_click_entry(event):
    logger.debug("Text Entered!")
    text = input_entry.get()
    input_entry.delete(0, tkinter.END)
    if text == "":
        return
    process(text)


def set_output(text):
    logger.debug("Setting output text: {}".format(text))
    print(text)
    output_text.config(text=text)


# Initializing pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


def search_wikipedia(text):
    if text == "":
        return
    if not is_internet_connected():
        speak("You are not connected to the internet!")
        return
    result = wikipedia.summary(text, sentences=2)
    speak(result)


def is_internet_connected():
    url = "http://www.google.com"
    timeout = 2
    try:
        requests.get(url, timeout=timeout)
        return True
    except (requests.ConnectionError, requests.Timeout):
        return False


def test_internet_speed():
    speak("Testing internet speed!")
    s = speedtest.Speedtest()
    s.get_best_server()
    ping = s.results.ping
    download = s.download() / 1024 / 1024
    upload = s.upload() / 1024 / 1024
    text = "Download speed: {:.2f} Mb/s" \
           "\nUpload speed: {:.2f} Mb/s" \
           "\nPing: {}".format(download, upload, ping)
    speak(text)


def search_google(text):
    chrome = webbrowser.get(using="chrome")
    chrome.open(text)


def play_music():
    pass


def play_on_youtube(text):
    pass


def open_app(name):
    pass


def tell_weather():
    pass


def tell_news():
    url = "http://newsapi.org/v2/top-headlines?country=us&apiKey={}".format(NEWSAPI)
    # url = "https://newsapi.org/v2/everything?q=Pakistan&sortBy=popularity&apiKey={}".format(NEWSAPI)
    page = requests.get(url)
    speak(page)


def tell_location():
    pass


def tell_schedule():
    df = pd.read_excel("schedule.xlsx")
    print(df)


def tell_assignment_quiz_from_portal():
    pass


def tell_latest_movies_from_yts():
    url = "https://yts.mx/api/v2/"
    parameters = '?limit=5'
    response = requests.get(url + "list_movies.json" + parameters)

    json_obj = response.json()
    movies = json_obj['data']['movies']
    latest_movies = []
    for m in movies:
        latest_movies.append(m['title_long'])
    speak("\n".join(latest_movies))
    # print(json.dumps(json_obj, sort_keys=True, indent=4))
    # print(json.loads(json_obj))


def lock_computer():
    speak("Computer locked!")
    cmd = 'rundll32.exe user32.dll, LockWorkStation'
    subprocess.call(cmd)


def shutdown_computer():
    speak("Shutting down computer in 5 seconds...")
    # os.system("shutdown /s /t 5")


def take_screenshot():
    pass


def set_reminder(text):
    pass


def tell_joke():
    speak(pyjokes.get_joke())


def tell_time():
    now_time = datetime.datetime.now().strftime('%I:%M %p')
    speak("The time is {}.".format(now_time))


def find_phone():
    pass


def tell_outlook_meetings():
    pass


def tell_phone_status():
    pass


def speak(text):
    logger.debug("Speaking: {}".format(text))
    if engine._inLoop:
        print("Engine is in loop!")
        engine.endLoop()
    set_output(text)
    engine.say(text)
    engine.runAndWait()


# Speaks out the received text
# def speak(text):
#     speak_td = threading.Thread(target=speak, args=(text,))
#     speak_td.start()
#     set_output(text)
#     engine.say(text)
#     engine.runAndWait()


def start_listen_thread():
    logger.debug("Starting listening thread...")
    listen_td = threading.Thread(target=listen)
    listen_td.start()


def listen():
    logger.debug("Listening...")
    playsound("sounds/wakeup_sound.wav")
    set_output("Listening...")
    if not is_internet_connected():
        logger.debug("Internet is not connected, listening with vosk...")
        print("Vosk: Listening...")
        mic_button.config(bg="red")
        # return vosk.listen()
        text = vosk.listen()
        playsound("sounds/stop_listening.wav")
        process(text)
    else:
        logger.debug("listening with Google...")
        print("Google: Listening...")
        mic_button.config(bg="green")
        r = sr.Recognizer()
        try:
            with sr.Microphone() as source:
                r.pause_threshold = 1
                # r.adjust_for_ambient_noise(source, duration=0.2)
                audio = r.listen(source)
                save_audio_file(audio)
            said = ""
            try:
                said = r.recognize_google(audio)
                print(said)
                playsound("sounds/stop_listening.wav")
            except sr.UnknownValueError:
                print("Unknown!")
                said = "Unknown"
            except sr.RequestError:
                print("No internet connection! Going offline mode!")
                mic_button.config(bg="red")
                said = vosk.listen()
            # return said.lower()
            process(said.lower())
        except OSError:
            print("No microphone!")


# def process(text):
#     process_td = threading.Thread(target=process_thread, args=(text,))
#     process_td.start()


def process(text):
    logger.debug("Processing ({})".format(text))
    playsound("sounds/thinking.wav")
    mic_button.config(bg="white")
    if text is None or text == "":
        return
    elif "who are you" in text:
        speak("I am {}. Your personal assistant. Ask me anything and i will do that for you!"
              .format(ASSISTANT_NAME))
    elif "how are you" in text:
        speak("I am fine, thanks! How are you?")
    elif "what can you do" in text:
        speak("I can do a lot of things like: Turn off PC\nLock PC")
    elif "what is the time now" in text:
        tell_time()
    elif "shutdown the computer" in text or "shutdown pc" in text:
        shutdown_computer()
    elif "lock the computer" in text or "lock pc" in text:
        lock_computer()
    elif "search wikipedia for " in text:
        search_wikipedia(text[21:])
    elif "check internet connection" in text or "is internet working" in text:
        if is_internet_connected():
            speak("The internet is working great!")
        else:
            speak("No internet connection!")
    elif "test internet speed" in text or "how is the internet" in text:
        test_internet_speed()
    elif "show me latest movies from yts" in text:
        tell_latest_movies_from_yts()
    elif "bye" in text:
        speak("Bye!")
        quit()
    elif "show me my schedule" in text:
        tell_schedule()
    elif "tell me a joke" in text:
        tell_joke()
    elif "show me top headlines" in text or "show me latest news" in text:
        tell_news()
    else:
        speak("I didn't understand. Please try again!")


def listen_wake_word():
    logger.debug("Listening for wake_word ({})".format(WAKE_WORD))
    while True:
        print("Listening for wake_word...")
        word = vosk.listen_wake_word()
        if WAKE_WORD in word:
            listen()


def save_audio_file(audio):
    time_str = time.strftime("%Y%m%d_%H%M%S")
    folder_name = "audio_history"
    filename = "{}/audio_{}.wav".format(folder_name, time_str)
    try:
        os.mkdir(folder_name)
    except OSError:
        pass
    with open(filename, "wb") as file:
        file.write(audio.get_wav_data())


# Getting configuration settings
config = configparser.ConfigParser()
config.read('config.ini')
# for s in config.sections():
#     print(s)
#     for k, v in enumerate(config[s]):
#         print(k, v)
settings = dict(config.items('SETTINGS'))
api_keys = dict(config.items('APIKEYS'))

first_time = settings["first_time"]
ASSISTANT_NAME = settings["assistant_name"]
USERNAME = settings["user_name"]
speech_rec = settings["speech_rec"]
WAKE_WORD = settings["wake_word"]
NEWSAPI = api_keys['newsapi']

s = json.dumps(settings, sort_keys=True, indent=4)
a = json.dumps(api_keys, sort_keys=True, indent=4)

logger.debug("Configurations loaded: \n{}\n{}".format(s, a))

if first_time == "true":
    pass


# tell_time()
# while True:
#     txt = listen_wake_word()
#     process(txt)


main_window = tkinter.Tk()
mic_img = tkinter.PhotoImage(file="images/mic.png")
mic_image = mic_img.subsample(10, 10)
main_window.title("Karen")
main_window.geometry("320x480-8+60")

main_frame = tkinter.Frame(main_window, border=1, background='green')
main_frame.pack(fill="both", expand=True)
bottom_frame = tkinter.Frame(main_window)
bottom_frame.pack(side="bottom", anchor="w", fill="x")

output_text = tkinter.Label(main_frame, text="Hi, how can i help you?")
output_text.config(font=("Calibri", 12, "bold"), wraplength="250")
output_text.pack(fill="both", expand=True)

input_entry = tkinter.Entry(bottom_frame, width="34")
input_entry.config(font="Calibri, 11")
input_entry.pack(side="left", ipady=7)
mic_button = tkinter.Button(bottom_frame, image=mic_image, width="50", height="30", relief="flat", command=on_click_mic)
mic_button.pack(side="right")

input_entry.focus()
input_entry.bind('<Return>', on_click_entry)

thread = threading.Thread(target=listen_wake_word)
thread.start()

main_window.mainloop()


# while True:
#     words = listen_wake_word()
#     process(words)
