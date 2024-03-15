import json


def get_json_file(link):
    with open(link, mode='r',encoding='utf-8') as f:
        return json.load(f)
