from os.path import basename
from utils.settings import KAREN_VERSION

name = basename(__file__[:-3])
enable = True
command = [
    [name, "karen_version", ["show karen version"]]
]


def karen_version(text):
    return "Karen version = "+KAREN_VERSION
