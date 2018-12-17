import json


def get_settings():
    with open("alyssum/settings.json", "rb") as f:
        data = json.load(f)
    return data


def set_settings(data):
    with open("alyssum/settings.json", "w") as f:
        f.write(json.dumps(data, sort_keys=True, indent=4, ensure_ascii=False))


def get_version_and_set_next():
    settings = get_settings()
    version_old = settings["version"]
    ar = version_old.split(".")
    version = ar.copy()
    version[2] = str(int(version[2])+1)
    settings["version"]=".".join(version)
    set_settings(settings)
    return version_old
