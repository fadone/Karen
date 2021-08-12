import os
import subprocess
import datetime
from os.path import basename
import clipboard
import pyautogui
import psutil

enable = True
name = basename(__file__[:-3])

command = [
    [name, "shutdown_pc", ["shutdown computer", "turn off computer", "shutdown pc", "turn off pc"]],
    [name, "restart_pc", ["restart pc", "restart computer"]],
    [name, "lock_pc", ["lock computer", "lock pc"]],
    [name, "logoff_pc", ["logoff pc", "sign out pc"]],
    [name, "launch_app", ["launch"]],
    [name, "take_screenshot", ["take screenshot"]],
    [name, "read_copied_text", ["read copied text"]],
    [name, "take_picture", ["take picture"]],
    [name, "system_stats", ["show system stats"]]
]


def shutdown_pc(text):
    os.system("shutdown /s /t 5")
    return "Shutting down computer in 5 seconds!"


def restart_pc(text):
    os.system("shutdown /r /t 5")
    return "Restarting computer in 5 seconds!"


def lock_pc(text):
    cmd = 'rundll32.exe user32.dll, LockWorkStation'
    subprocess.call(cmd)
    return "Computer locked!"


def logoff_pc(text):
    subprocess.call(["shutdown", "/l /t 5"])
    return "Logging off in 5 seconds"


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


def read_copied_text(text):
    t = clipboard.paste()
    return t


def take_picture(text):
    ec.capture(0,"robo camera","img.jpg")


def system_stats(text):
    cpu = psutil.cpu_percent(4)
    ram = psutil.virtual_memory()[2]
    return "CPU: {}%\nRAM: {}%".format(str(cpu), str(ram))

