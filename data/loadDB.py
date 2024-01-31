import json


def load_json():
    with open('C:/telegram-bot/data/db.json') as f:
        folders = json.load(f)
        return folders['folders']