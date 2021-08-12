from os.path import basename
import requests, json

name = basename(__file__[:-3])

command = [
    [name, "get_weather", ["how is the weather in"]],
]
enable = True


def get_weather(text):
    city = text.split("in")[1].strip()

    pass
