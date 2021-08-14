import difflib
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk
from nltk.corpus import stopwords

from skills import about
from skills import android
from skills import answer
from skills import bluetooth
from skills import configuration
from skills import cuonline
from skills import internet
from skills import news
from skills import note
from skills import pc
from skills import script
from skills import tv
from skills import weather
from skills import whatsapp
from skills import wifi
from skills import wiki
from skills import yts
from skills import schedule
from skills import word_dictionary
from skills import compute
from skills import music
from skills import location
from skills import browser

from os.path import dirname, basename, isfile, join
import glob


def get_commands_list():
    try:
        mod = glob.glob(join(dirname(__file__), "*.py"))
        all_skills = [basename(f)[:-3] for f in mod if isfile(f) and not f.endswith('__init__.py')]
        # commands_list = [x for x in [eval(x+".command") for x in all_skills] if x != []]
        commands_list = [x for x in [eval(x+".command") for x in all_skills if eval(x+".enable")] if x != []]
        return commands_list
    except AttributeError as e:
        print(e)
        return False


def get_all_commands():
    all_commands = []
    for module_func_commands in get_commands_list():
        for module_func_command in module_func_commands:
            commands = module_func_command[2]
            # for command in commands:
            #     COMMANDS_LIST.append(command)
            all_commands += commands
    return all_commands


def execute(text):
    # commands_list = get_commands_list()
    commands_list = sorted(get_commands_list(), key=len, reverse=True)
    if not commands_list:
        return "No skills found!"
    for module_func_commands in commands_list:
        for module_func_command in module_func_commands:
            commands = module_func_command[2]
            for command in commands:
                if command in text:
                    mod_name = module_func_command[0]
                    func_name = module_func_command[1]
                    func = mod_name + "." + func_name + "('" + text + "')"
                    return eval(func)
    com_list = get_all_commands()
    # mean = difflib.get_close_matches(s)
    similar = search_similar(text, com_list)
    if not similar:
        return False
    return "Did you mean:\n" + "\n".join(similar)


def search_similar(command_str, all_command_list):
    # command_list = command_str.split()
    # print(command_list)
    # print(all_command_list)

    similar = []
    for commands in all_command_list:
        if command_str in commands:
            similar.append(commands)
    return similar
