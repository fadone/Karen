import configparser


def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    for s in config.sections():
        print(s)
        for k, v in enumerate(config[s]):
            print(k, v)
    first_time = config.get("first_time")
    assistant_name = config.get("assistant_name")
    user_name = config.get("user_name")
    speech_rec = config.get("speech_rec")
    if first_time == "true":
        pass




load_config()
