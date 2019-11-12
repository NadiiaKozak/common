import json


def get_data(item_list):
    try:
        with open(item_list) as files1:
            return json.load(files1)
    except(IOError, ValueError, FileNotFoundError, json.JSONDecodeError):
        return []


def add_data(data, item_list):
    try:
        with open(item_list, 'w', encoding='utf-8') as files1:
            return json.dump(data, files1, ensure_ascii=False, indent=4)
    except ValueError:
        return item_list
