import configparser
from os.path import basename

name = basename(__file__[:-3])
command = [
    [name, "set_config", ["set config"]],
    [name, "read_config", ["get config"]],
]
enable = True


def read_config(text):
    option = text.split()[2]
    config = configparser.ConfigParser()
    config.read('config.ini')
    options = config.options("SETTINGS")
    if option in options:
        return config["SETTINGS"][option]
    else:
        return "No such option {}".format(option)


def set_config(text):
    try:
        option = text.split()[2].strip()
        value = text.split("to")[1].strip()
        config = configparser.ConfigParser()
        config.read('config.ini')
        options = config.options("SETTINGS")
        if option in options:
            # config.set("SETTINGS", option, value)
            config["SETTINGS"][option] = value
            with open('config.ini', 'w') as configfile:
                config.write(configfile)
            return "Configuration updated!"
        else:
            return "Error updating configuration! No such option {}".format(option)
    except IndexError:
        return "Wrong command! Please try again."
