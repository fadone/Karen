import configparser

# import skills as skill

# commands_list = skill.get_all_commands()

wake_word_sound = "sounds/wakeup_sound.wav"
thinking_sound = "sounds/thinking.wav"
stop_listen_sound = "sounds/stop_listening.wav"

KAREN_VERSION = "v0.2"


class MyConfiguration:
    config = None

    def __init__(self):
        self.config = configparser.ConfigParser()
        self.config.read("utils/config.ini")
        self.first_time = self.config["SETTINGS"]["first_time"]
        self.wake_word = self.config["SETTINGS"]["wake_word"]
        self.username = self.config["SETTINGS"]["username"]
        self.speech_rec = self.config["SETTINGS"]["speech_rec"]
        self.assistant_name = self.config["SETTINGS"]["assistant_name"]

        self.news_api = self.config["API_KEYS"]["news_api"]
        self.open_weather = self.config["API_KEYS"]["open_weather"]
        self.open_location = self.config["API_KEYS"]["open_location"]
        self.wolframalpha = self.config["API_KEYS"]["wolframalpha"]

    def read_config(self, section, option):
        options = self.config.options(section)
        # if option in options:
        return self.config[section][option]
        # return None

    def set_config(self, section, option, value):
        # try:
        #     options = self.config.options(section)
        #     if option in options:
        self.config[section][option] = value
        with open('utils/config.ini', 'w') as configfile:
            self.config.write(configfile)
            # return True
            # else:
            #     return False
        # except IndexError:
        #     return False

# config = configparser.ConfigParser()
# config.read('config.ini')
# settings = config.sections()[0]
# api_keys = config.sections()[1]
#
# # Getting Configurations
# first_time = config[settings]["first_time"]
# wake_word = config[settings]["wake_word"]
# username = config[settings]["username"]
# speech_rec = config[settings]["speech_rec"]
# assistant_name = config[settings]["assistant_name"]
#
# # Getting API Keys
# news_api = config[api_keys]["news_api"]
# open_weather = config[api_keys]["open_weather"]
# open_location = config[api_keys]["open_location"]
