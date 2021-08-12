from vosk import Model, KaldiRecognizer
import pyaudio
import json
from utils.settings import MyConfiguration


def listen():
    # Speech Recognition
    model = Model("utils/model")
    rec = KaldiRecognizer(model, 16000)

    # Opens microphone for listening.
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
    stream.start_stream()

    while True:
        data = stream.read(2048)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # result is a string
            result = rec.Result()
            # convert it to a json/dictionary
            result = json.loads(result)
            text = result['text']
            return text


def listen_wake_word():
    # Speech Recognition
    config = MyConfiguration()
    wake_word = config.wake_word
    model = Model("utils/model")
    rec = KaldiRecognizer(model, 16000, '["' + wake_word + '"]')

    # Opens microphone for listening.
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
    stream.start_stream()

    while True:
        data = stream.read(2048)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # result is a string
            result = rec.Result()
            # convert it to a json/dictionary
            result = json.loads(result)
            text = result['text']
            if text == "hey karen":
                return text
            # return text
