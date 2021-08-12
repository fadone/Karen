import configparser
from os.path import basename
from utils.settings import MyConfiguration

name = basename(__file__[:-3])
command = [
    [name, "set_config", ["set config"]],
    [name, "read_config", ["get config"]],
]
enable = True


def read_config(text):
    try:
        option = text.split()[2]
        config = MyConfiguration()
        try:
            value = config.read_config("SETTINGS", option)
            return value
        except KeyError:
            return "No key found: {}".format(option)
    except IndexError:
        return "Wrong command!"
    # config = configparser.ConfigParser()
    # config.read('config.ini')
    # options = config.options("SETTINGS")
    # if option in options:
    #     return config["SETTINGS"][option]
    # else:
    #     return "No such option {}".format(option)


def set_config(text):
    try:
        option = text.split()[2].strip()
        value = text.split("to")[1].strip()
        config = MyConfiguration()
        config.set_config("SETTINGS", option, value)
        return "Configuration saved!"
    except IndexError:
        return "Wrong command!"
    #     config = configparser.ConfigParser()
    #     config.read('config.ini')
    #     options = config.options("SETTINGS")
    #     if option in options:
    #         # config.set("SETTINGS", option, value)
    #         config["SETTINGS"][option] = value
    #         with open('config.ini', 'w') as configfile:
    #             config.write(configfile)
    #         return "Configuration updated!"
    #     else:
    #         return "Error updating configuration! No such option {}".format(option)
    # except IndexError:
    #     return "Wrong command! Please try again."
