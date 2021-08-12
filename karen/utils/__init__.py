import requests
import winsound


def play_sound(path):
    winsound.PlaySound(path, winsound.SND_ASYNC | winsound.SND_ALIAS)


def check_internet():
    # logger.debug("Checking internet connection...")
    url = "http://www.kite.com"
    timeout = 2
    try:
        requests.get(url, timeout=timeout)
        # logger.debug("Internet is connected!")
        return True
    except (requests.ConnectionError, requests.Timeout) as exception:
        # logger.debug("Internet is disconnected!")
        return False
