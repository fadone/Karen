import os
import subprocess
import time
from os.path import basename
from pynput.keyboard import Key, Controller

name = basename(__file__[:-3])
enable = True
command = [
    [name, "play_music", ["play music"]]
]


def play_music(text):
    os.system('cmd /c "start mswindowsmusic:"')
    time.sleep(1)
    keyboard = Controller()
    keyboard.press(Key.enter)
    return "Playing Music"
