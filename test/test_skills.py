import wikipedia


def search_wikipedia(text):
    result = wikipedia.summary(text, sentences=2)
    print(result)


search_wikipedia("Pakistan")
