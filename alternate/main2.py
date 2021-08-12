import json
import os
import subprocess
import time
import pyttsx3
import requests
import wikipedia
import speech_recognition as sr
import utils.vosk_listen as vosk
from playsound import playsound
import speedtest
import requests
import webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

assistant_name = "Karen"
wake_word = "hey {}".format(assistant_name.lower())


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
    download = s.download()/1024/1024
    upload = s.upload()/1024/1024
    text = "Download speed: {:.2f} Mb/s" \
           "\nUpload speed: {:.2f} Mb/s" \
           "\nPing: {}".format(download, upload, ping)
    speak(text)


def search_google(text):
    chrome = webbrowser.get(using="chrome")
    chrome.open(text)


def play_music():
    pass4nnnnnnx


def play_on_youtube(text):
    pass


def open_app(name):
    pass


def tell_weather():
    pass


def tell_news():
    pass


def tell_location():
    pass


def tell_schedule():
    pass


def tell_assignment_quiz_from_portal():
    pass


def tell_latest_movies_from_yts():
    url = "https://yts.mx/api/v2/"
    parameters = '?limit=5'
    response = requests.get(url+"list_movies.json"+parameters)

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
    os.system("shutdown /s /t 5")


def take_screenshot():
    pass


def set_reminder(text):
    pass


def tell_joke():
    pass


def tell_time():
    now_time = time.time()
    speak(now_time)


def find_phone():
    pass


def tell_outlook_meetings():
    pass


def tell_phone_status():
    pass


# Speaks out the received text
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def listen():
    if not is_internet_connected():
        print("Vosk: Listening...")
        return vosk.listen()
    print("Google: Listening...")
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
        except sr.RequestError:
            speak("No internet connection! Going offline mode!")
            said = vosk.listen()
        return said.lower()
    except OSError:
        print("No microphone!")


def process(text):
    if text is None or text == "":
        return
    elif "who are you" in text:
        speak("I am {}. Your personal assistant. Ask me anything and i will do that for you!".format(assistant_name))
    elif "how are you" in text:
        speak("I am fine, thanks! How are you?")
    elif "what can you do" in text:
        speak("I can do a lot of things like: Turn off PC\nLock PC")
    elif "what is time now" in text:
        tell_time()
    elif "shutdown the computer" or "turn off pc" in text:
        shutdown_computer()
    elif "lock the computer" or "lock pc" in text:
        lock_computer()
    elif "search wikipedia for " in text:
        search_wikipedia(text[21:])
    elif "check internet connection" in text:
        if is_internet_connected():
            speak("The internet is working great!")
        else:
            speak("No internet connection!")
    elif "test internet speed" in text:
        test_internet_speed()
    elif "bye" in text:
        speak("Bye!")
        quit()
    else:
        speak("I didn't understand. Please try again!")


def listen_wake_word():
    while True:
        print("Listening for wake_word...")
        word = vosk.listen_wake_word()
        if wake_word in word:
            playsound("sounds/wakeup_sound.wav")
            return listen()
        if "key_pressed" in word:
            return input("Text: ")


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


# tell_time()
# while True:
#     txt = listen_wake_word()
#     process(txt)

