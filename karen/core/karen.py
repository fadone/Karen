from karen.engine import tts
from karen.engine import stt


def listen_process_thread():
    text = stt.listen()
    process(text)


def process_thread(text):
    process(text)


def process(text):
    pass
