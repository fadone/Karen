from vosk import Model, KaldiRecognizer
import pyaudio
import json


def listen():
    # Speech Recognition
    model = Model("model")
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
            print(text)
            # return text


def listen_wake_word():
    # Speech Recognition
    model = Model("model")
    rec = KaldiRecognizer(model, 16000, '["hey karen"]')

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
            print(text)
            # return text


# print(listen())
listen_wake_word()
