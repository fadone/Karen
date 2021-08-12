from os.path import basename
import requests, json
from utils.settings import MyConfiguration
from utils.controller import check_internet

name = basename(__file__[:-3])

command = [
    [name, "get_weather", ["how is the weather in"]],
]
enable = True


def get_weather(text):
    city = text.split("in")[1].strip()
    if not check_internet():
        return "No internet connection!"
    config = MyConfiguration()
    api_key = config.open_weather
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(complete_url)
    x = response.json()
    degree_sign = u'\N{DEGREE SIGN}'
    if x["cod"] != "404":
        y = x["main"]
        info = x["sys"]
        country = info["country"]
        current_temp = str(y["temp"]) + degree_sign + "C"
        current_pressure = str(y["pressure"])
        current_humidity = str(y["humidity"])
        feels_like = str(y["feels_like"]) + degree_sign + "C"
        min_temp = y["temp_min"]
        max_temp = y["temp_max"]
        z = x["weather"]
        weather_description = z[0]["description"]
        data = "Weather in {}, {}:" \
               "\nDescription: {}" \
               "\nTemperature: {}" \
               "\nFeels like: {}" \
               "\nHumidity: {}%" \
               "\nAtmospheric pressure(hPa): {}".format(city, country, weather_description, current_temp, feels_like, current_humidity, current_pressure)



        # data = " Temperature (in kelvin unit) = " + \
        #        str(current_temperature) + \
        #        "\n atmospheric pressure (in hPa unit) = " + \
        #        str(current_pressure) + \
        #        "\n humidity (in percentage) = " + \
        #        str(current_humidity) + \
        #        "\n description = " + \
        #        str(weather_description)
        return data
    else:
        return " City Not Found "
