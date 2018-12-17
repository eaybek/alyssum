import json
import pprint
from alyssum.settings import SETTINGS


def get_settings():
    return SETTINGS


def set_settings(data):
    with open("alyssum/settings.py", "w") as f:
        f.write("SETTINGS = " + pprint.pformat(data))


def get_version_and_set_next():
    settings = get_settings()
    version_old = settings["version"]
    ar = version_old.split(".")
    version = ar.copy()
    version[2] = str(int(version[2])+1)
    settings["version"]=".".join(version)
    set_settings(settings)
    return version_old
