import pyttsx3
import utils.vosk_listen as vosk;
import datetime
import wikipedia
import speech_recognition as sr
import webbrowser as web

# speaks out the received text using pyttsx3
def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


def listen_google():
    print("Listening...")
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 1
            audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError as e:
            print(e)
        except sr.RequestError:
            return listen_vosk()
        return said.lower()
    except OSError:
        speak("You don't have microphone.")


def listen_vosk():
    print("Offline mode!")
    words = vosk.listen()
    return words


def listen_wake_word():
    while True:
        print("Listening for wake word...")
        w = vosk.listen_wake_word()
        if w == "hey karen":
            words = listen_google()
            return words


# process the received text, perform action and returns the response
def brain(text):
    if "who are you" in text:
        return "I am Karen. Your personal assistant. I can do a lot of things. Ask me anything!"
    elif "what can you do" in text:
        return "Here is the list of things i can do:\n" \
               "Take Notes\n"
    elif "shut down" in text:
        quit()
    elif "search wikipedia" in text:
        search_wikipedia(text[17:])
    else:
        return "I didn't understand that!"


# generates the greetings according to time of the day
def greetings():
    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        return "Good Morning Hisham!"
    elif 12 <= hour < 18:
        return "Good Afternoon Hisham!"
    else:
        return "Good Evening Hisham!"


# Karen Skills
def play_music():
    pass


def take_note():
    pass


def search_wikipedia(text):
    result = wikipedia.summary(text)
    return result


def google_search():
    pass


def say_time():
    pass


def weather():
    pass


def pc():
    pass


def open_app():
    pass


def send_whatsapp_message():
    user_name = {
        'Hisham': '+923088806636'
    }
    try:
        output("To whom you want to send the message?")
        name = inputCommand()
        output("What is the message")
        we.open("https://web.whatsapp.com/send?phone=" +
                user_name[name]+'&text='+inputCommand())
        sleep(6)
        pyautogui.press('enter')
        output("Message sent")
    except Exception as e:
        print(e)
        output("Unable to send the Message")

# Initializing
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

# Start
speak(greetings())
while True:
    command = listen_wake_word()
    response = brain(command)
    speak(response)


