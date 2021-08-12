import requests

speak = None
listen = None
play_sound = None


def check_internet():
    url = "http://www.google.com"
    timeout = 3
    try:
        requests.get(url, timeout=timeout)
        # logger.debug("Internet is connected!")
        return True
    # except (requests.ConnectionError, requests.Timeout) as exception:
    except Exception as e:
        # logger.debug("Internet is disconnected!")
        print(e)
        return False
