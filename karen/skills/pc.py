import os
import subprocess
import datetime
from os.path import basename
import clipboard

import pyautogui

enable = True
name = basename(__file__[:-3])

command = [
    [name, "shutdown_pc", ["shutdown computer", "turn off computer", "shutdown pc", "turn off pc"]],
    [name, "lock_pc", ["lock computer", "lock pc"]],
    [name, "launch_app", ["launch"]],
    [name, "take_screenshot", ["take screenshot"]],
    [name, "read_text_from_screen", ["read text from screen", "read selected text"]]
]


def shutdown_pc(text):
    os.system("shutdown /s /t 5")
    return "Shutting down computer in 5 seconds!"


def lock_pc(text):
    cmd = 'rundll32.exe user32.dll, LockWorkStation'
    subprocess.call(cmd)
    return "Computer locked!"


def launch_app(text):
    app = text.split()[1] + ".exe"
    subprocess.call(app)
    return "Launching {}".format(app)


def take_screenshot(text):
    current_time = datetime.datetime.now().strftime("%H-%M-%S")
    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
    screenshot = pyautogui.screenshot()
    print(desktop)
    screenshot.save(desktop+"\screenshot-"+current_time+".png")
    return "Screenshot taken!"


def read_text_from_screen(text):
    t = clipboard.paste()
    return t
