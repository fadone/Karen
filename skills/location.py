from os.path import basename

import requests

name = basename(__file__[:-3])
enable = True
command = [
    [name, "my_location", ["where am i"]]
]


def my_location(text):
    ip_add = requests.get('https://api.ipify.org').text
    url = 'https://get.geojs.io/v1/ip/geo/' + ip_add + '.json'
    geo_requests = requests.get(url)
    geo_data = geo_requests.json()
    print(geo_data)
    city = geo_data['city']
    state = geo_data['region']
    country = geo_data['country']
    print(city, state, country)
