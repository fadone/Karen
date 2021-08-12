from os.path import basename
from sonybraviaremote import TV, TVConfig
import threading

name = basename(__file__[:-3])
command = [
    [name, "connect_tv", ["connect tv"]],
    [name, "channel_up", ["change tv channel"]],
    [name, "volume_up", ["turn up tv volume"]],
    [name, "volume_down", ["turn down tv volume"]],
    [name, 'turn_on_tv', ["turn on tv"]],
    [name, 'turn_off_tv', ["turn off tv"]],
]
enable = True

tv = None


def connect():
    global tv
    if tv is not None and tv.is_on():
        return True
    else:
        try:
            config = TVConfig('192.168.146.205', 'Karen')
            tv = TV.connect(config, on_auth)
            if tv.is_on():
                return True
            else:
                return False
        except Exception as e:
            print(e)
            return False


def on_auth():
    return input('Pincode: ')


def connect_tv(text):
    global tv
    if tv is not None and tv.is_on():
        return "TV is connected!"
    else:
        config = TVConfig('192.168.146.205', 'Karen')
        tv = TV.connect(config, on_auth)
        if tv.is_on():
            return "TV connected!"
        else:
            return "Error connecting tv, make sure TV is plugged in and connected to same WIFI."


def turn_on_tv(text):
    if tv is not None and tv.is_on():
        tv.wake_up()
        return "Turning on TV..."
    else:
        return "TV not connected!"


def turn_off_tv(text):
    if tv is not None and tv.is_on():
        tv.power_off()
        return "Turning off TV..."
    else:
        return "TV not connected!"


def channel_up(text):
    if tv is not None and  tv.is_on():
        tv.next_channel()
        return "Changing channel..."
    else:
        return "TV not connected!"


def channel_down(text):
    if tv is not None and  tv.is_on():
        tv.previous_channel()


def volume_up(text):
    if tv is not None and tv.is_on():
        tv.volume_up()
        return "Turning up volume..."
    else:
        return "TV not connected!"


def volume_down(text):
    if tv is not None and tv.is_on():
        tv.volume_down()
        return "Turning down volume..."
    else:
        return "TV not connected!"

