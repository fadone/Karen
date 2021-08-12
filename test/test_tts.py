import pyttsx3


def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()


engine = pyttsx3.init()
voices = engine.getProperty('voices')
for voice in voices:
    print(voice)
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)
speak("Hi! My name is Karen! I am your personal digital assistant! I will help you with anything! Just say 'hey "
      "karen' and ask me and I will do my best.")
