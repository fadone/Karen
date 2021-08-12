import wave
from datetime import datetime

from vosk import Model, KaldiRecognizer
import pyaudio
import json


def listen():
    filename = "audio/{}.wav".format(datetime.now().strftime("%m/%d/%Y-%H:%M:%S"))
    stream_format = pyaudio.paInt16
    channels = 1
    rate = 16000
    frames_per_buffer = 4096

    # Speech Recognition
    model = Model("model")
    rec = KaldiRecognizer(model, 16000)

    # Opens microphone for listening.
    p = pyaudio.PyAudio()
    stream = p.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=4096)
    stream.start_stream()
    frames = []

    while True:
        data = stream.read(2048)
        frames.append(data)
        if len(data) == 0:
            break
        if rec.AcceptWaveform(data):
            # result is a string
            result = rec.Result()
            # convert it to a json/dictionary
            result = json.loads(result)
            text = result['text']
            print(text)

            wf = wave.open(filename, 'wb')
            wf.setnchannels(channels)
            wf.setsampwidth(p.get_sample_size(stream_format))
            wf.setframerate(rate)
            wf.writeframes(b''.join(frames))
            wf.close()


listen()
