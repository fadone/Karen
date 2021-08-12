from os.path import basename
from PyDictionary import PyDictionary
from utils.controller import check_internet

name = basename(__file__[:-3])
enable = True
command = [
    [name, "define_word", ["define"]],
    [name, "synonym", ["synonym of"]],
    [name, "antonym", ["antonym of"]],
]


def define_word(text):
    try:
        word = text.split()[1]
    except IndexError:
        return "Specify word!"
    if check_internet():
        dictionary = PyDictionary()
        meaning_dict = dictionary.meaning(word)
        return_str = ""
        if not meaning_dict:
            return "Wrong spelling!"
        for m in meaning_dict.items():
            word_type = "\n" + m[0]
            define_list = [x for x in m[1]]
            return_str += word_type + ":\n- " + "\n- ".join(define_list) + "\n"
        return return_str
    else:
        return "No internet connected!"


def synonym(text):
    try:
        word = text.split()[2]
    except IndexError:
        return "Specify word!"
    if check_internet():
        dictionary = PyDictionary()
        synonym_dict = dictionary.synonym(word)
        return_str = ""
        if not synonym_dict:
            return "No synonyms for this word!"
        print(synonym_dict)
    else:
        return "No internet connected!"


def antonym(text):
    try:
        word = text.split()[2]
    except IndexError:
        return "Specify word!"
    if check_internet():
        dictionary = PyDictionary()
        antonyms_dict = dictionary.antonym(word)
        return_str = ""
        if not antonyms_dict:
            return "No antonyms for this word!"
        print(antonyms_dict)
    else:
        return "No internet connected!"
