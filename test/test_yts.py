import requests


def tell_latest_movies_from_yts():
    url = "https://yts.mx/api/v2/"
    response = requests.get(url+"list_movies.json")
    json_obj = response.json()
    movies = json_obj['data']['movies']
    for movie in movies:
        print(movie['title_long'])
    print(movies)
    # print(json.dumps(json_obj, sort_keys=True, indent=4))
    # print(json.loads(json_obj))


tell_latest_movies_from_yts()