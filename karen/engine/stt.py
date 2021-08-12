# from karen.utils import vosk_listen as vosk
import speech_recognition as sr
import karen.utils as utils
import karen.utils.settings as settings
import karen.app as app

speech_rec = "both"


def listen_vosk():
    # logger.debug("Vosk: Listening...")
    # mic_button.config(bg="red")
    # text = vosk.listen()
    # print_output(text)
    # play_sound(stop_listen_sound)
    # mic_button.config(bg="white")
    # logger.debug("Vosk: Listened: {}".format(text))
    # return text
    pass


def listen_google():
    # logger.debug("Google: Listening...")
    utils.play_sound(settings.wakeup_sound)
    app.set_output_text("Listening...")
    r = sr.Recognizer()
    try:
        with sr.Microphone() as source:
            # mic_button.config(bg="green")
            app.set_mic_btn_color("green")
            r.energy_threshold = 4000
            audio = r.listen(source)
            # mic_button.config(bg="white")
            app.set_mic_btn_color("white")
            utils.play_sound(settings.stop_listen_sound)
        said = ""
        try:
            # play_sound(thinking_sound)
            utils.play_sound(settings.thinking_sound)
            app.set_output_text("Recognizing...")
            # print_output("Recognizing...")
            said = r.recognize_google(audio)
            # print_output(said)
            app.set_output_text(said)
        except sr.UnknownValueError as e:
            # print_output("Sorry, I didn't hear anything! Please try again!")
            # logger.error(e)
            pass
        except sr.RequestError as e:
            # print_output("No internet connection!")
            # logger.error(e)
            pass
        # play_sound(stop_listen_sound)
        # logger.debug("Google: Listened: {}!".format(said))
        return said.lower()
    except sr.WaitTimeoutError as e:
        # play_sound(stop_listen_sound)
        # print_output("Sorry, I didn't hear anything! Please try again!")
        # speak("Sorry, I didn't hear anything! Please try again!")
        pass
    except OSError as e:
        # print_output("Please check your microphone!")
        # logger.error(e)
        pass


def check_internet():
    return True


def listen():
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
        # print_output("No STT engine found: {}".format(speech_rec))
        pass