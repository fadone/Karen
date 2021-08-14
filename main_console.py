import pyttsx3
import requests
import utils.vosk_STT as vosk
import winsound
import utils.settings as util
import speech_recognition as sr
import database
import datetime
import skills


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def listen_vosk():
    text = vosk.listen()
    play_sound(util.stop_listen_sound)
    return text


def listen_google():
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.energy_threshold = 4000
            audio = r.listen(source)
        said = ""
        try:
            play_sound(util.thinking_sound)
            print("Recognizing...")
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError as e:
            speak("Sorry, I didn't hear anything! Please try again!")
        except sr.RequestError as e:
            speak("You don't have internet connection! Try enabling the speech_rec to 'both' or 'vosk'.!")
        play_sound(util.stop_listen_sound)
        return said.lower()
    except sr.WaitTimeoutError as e:
        play_sound(util.stop_listen_sound)
        speak("Sorry, I didn't hear anything! Please try again!")
    except OSError as e:
        speak("Please check your microphone!")


def listen():
    # logger.debug("Listening...")
    config = util.MyConfiguration()
    speech_rec = config.speech_rec
    print("Listening...")
    play_sound(util.wake_word_sound)
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
        print("No STT engine found: {}".format(speech_rec))


def process(text):
    # logger.debug("Processing: {}".format(text))
    if text is None or text == "":
        return
    response = skills.execute(text)
    if response:
        speak(response)
    else:
        speak("Sorry, I didn't understand! Please try again!")
    command = database.CommandDatabase()
    command.add_command(text, response, datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))


def play_sound(path):
    winsound.PlaySound(path, winsound.SND_ASYNC | winsound.SND_ALIAS)


def check_internet():
    url = "http://www.google.com"
    timeout = 2
    try:
        requests.get(url, timeout=timeout)
        return True
    except Exception as e:
        print(e)
        return False


def listen_process():
    text = listen()
    process(text)


def start():
    conf = util.MyConfiguration()
    username = conf.username
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning\n{}!".format(username))
    elif 12 <= hour < 18:
        speak("Good Afternoon\n{}!".format(username))
    else:
        speak("Good Evening\n{}!".format(username))


# Initializing pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

config = util.MyConfiguration()
wake_word = config.wake_word
start()
while True:
    print("Listening for wake_word...")
    word = vosk.listen_wake_word()
    if wake_word in word:
        listen_process()
