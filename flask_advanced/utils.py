import json




def get_data(item_list):
    with open(item_list) as file1:
        return json.load(file1)


def add_data(data, item_list):
    with open(item_list, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


