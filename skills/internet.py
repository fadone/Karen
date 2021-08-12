import time

import requests
import speedtest
from utils import controller as con
from utils import settings as st


command = [
    ["internet", "check_internet", ["check internet", "check internet connection", "how is the internet"]],
    ["internet", "test_internet_speed", ["test internet speed", "check internet speed"]]
]
enable = True


def check_internet(text):
    url = "http://www.google.com"
    timeout = 2
    try:
        requests.get(url, timeout=timeout)
        return "The internet is working great!"
    except (requests.ConnectionError, requests.Timeout) as exception:
        return "Internet is not working!"


def test_internet_speed(text):
    # from karen_optimized import speak
    con.speak("Testing internet speed...")
    con.play_sound(st.thinking_sound)
    s = speedtest.SpeedTest()
    s.get_best_server()

    ping = s.results.ping
    download = s.download() / 1024 / 1024
    upload = s.upload() / 1024 / 1024
    text = "Download speed: {:.2f} Mb/s" \
           "\nUpload speed: {:.2f} Mb/s" \
           "\nPing: {}".format(download, upload, ping)
    speak(text)
