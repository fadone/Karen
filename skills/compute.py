from os.path import basename
import wolframalpha
from utils.settings import MyConfiguration
from utils.controller import check_internet

name = basename(__file__[:-3])
enable = True
command = [
    [name, "compute", ["compute", "think", "question"]]
]


def compute(text):
    if "compute" in text:
        question = text.replace("compute ", "")
    elif "think" in text:
        question = text.replace("think ", "")
    elif "question" in text:
        question = text.replace("question ", "")
    else:
        question = text
    if not check_internet():
        return "No internet connection!"
    config = MyConfiguration()
    api_key = config.wolframalpha
    client = wolframalpha.Client(api_key)
    res = client.query(question)
    answer = next(res.results).text
    return answer
