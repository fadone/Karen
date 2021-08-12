from os.path import basename

name = basename(__file__[:-3])
command = [
    [name, "get_latest_movies", ["show me latest movies from yts"]]
]
enable = True


def get_latest_movies(text):
    pass
