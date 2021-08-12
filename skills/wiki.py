from os.path import basename

import wikipedia

name = basename(__file__[:-3])

command = [
    [name, "search_wikipedia", ["search wikipedia for "]]
]
enable = True


def search_wikipedia(text):
    topic = text.split("for")[1].strip()
    try:
        # info = str(ny.content[:500].encode('utf-8'))
        # res = re.sub('[^a-zA-Z.\d\s]', '', info)[1:]
        res = wikipedia.summary(topic, sentences=3)

        return res
    except Exception as e:
        print(e)
        return "Sorry, something went wrong. Check your internet connection!"

