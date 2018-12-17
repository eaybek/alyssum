import json

with open("/settings.json", "rb") as f:
    SETTINGS = json.load(f)

version = SETTINGS["version"]
