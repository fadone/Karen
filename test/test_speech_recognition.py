import speech_recognition as sr


def listen():
    print("Listening...")
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            r.pause_threshold = 1
            r.adjust_for_ambient_noise(source, duration=0.2)
            audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except sr.UnknownValueError as e:
            print("Unknown!")
        except sr.RequestError:
            print("Internet connection error!")
        return said.lower()
    except OSError:
        print("No microphone!")


while True:
    listen()
