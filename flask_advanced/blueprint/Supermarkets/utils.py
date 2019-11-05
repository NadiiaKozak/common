import json


def get_data():
    with open("blueprint/Supermarkets/data.json") as file1:
        return json.load(file1)


def add_data(data):
    with open("blueprint/Supermarkets/data.json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

