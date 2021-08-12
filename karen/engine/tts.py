import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)


def speak(text):
    # global reset_thread
    # logger.debug("Speaking: {}...".format(text))
    # if engine._inLoop:
    #     print("Engine is in loop!")
    #     engine.endLoop()
    # print_output(text)
    engine.say(text)
    engine.runAndWait()
    # logger.debug("Speaking: {} finished!".format(text))
    # if reset_thread is not None and reset_thread.is_alive():
    #     reset_thread.cancel()
    # else:
    #     reset_thread = threading.Timer(30.0, reset_output)
    #     reset_thread.start()
