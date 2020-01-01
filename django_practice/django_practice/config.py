import requests

POCKEMON_URL = 'https://pokeapi.co/api/v2/'


def get_pockemon():
    response = requests.get(f'{POCKEMON_URL}/type/3')
    return response.json()
