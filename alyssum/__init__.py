from .settings import SETTINGS
from . import decorators
version = SETTINGS["version"]


def initialize():
    print("Version : {}".format(version))
    decorators.counter_list = []
