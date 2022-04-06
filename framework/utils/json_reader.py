import json


def get_json(path):
    json_file = open(path, encoding="UTF-8")
    content = json.load(json_file)
    return content
