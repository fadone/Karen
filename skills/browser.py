from os.path import basename
# import pywhatkit as kt
import webbrowser

name = basename(__file__[:-3])
enable = True
command = [
    [name, "search_google", ["search google"]],
    [name, "search_youtube", ["search youtube"]],

]


def search_google(text):
    query = text.split("google ")[1]
    url = 'https://www.google.com/search?q={}'.format(query)
    webbrowser.open(url)
    return "Searching google for {}".format(query)


def search_youtube(text):
    query = text.split("youtube ")[1]
    # kt.playonyt(query)
    url = 'https://www.youtube.com/results?q={}'.format(query)
    webbrowser.open(url)
    return "Searching {} on Youtube".format(query)
