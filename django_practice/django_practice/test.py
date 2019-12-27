from http import HTTPStatus
import requests
from django.test import TestCase
from django.test import Client

from django.urls import reverse
from pytest import raises

from .views import POCKEMON_URL


class StatusViewTests(TestCase):
    client = Client()

    def test_health_check_view(self):
        response = self.client.get(reverse('health_check'))
        assert response.status_code == HTTPStatus.OK

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        assert response.status_code == HTTPStatus.OK

    def test_pokemons_view(self):
        response = self.client.get(reverse('pokemons'))
        assert response.status_code == HTTPStatus.OK

    def test_pokemons_type(self):
        response = requests.get(f'{POCKEMON_URL}/type/3')
        actual_result = type(response.json())
        result = type(dict())
        assert result == actual_result

    def test_pokemons_key_error(self):
        key_pokemon_url = 'name'
        response = requests.get(f'{POCKEMON_URL}/type/3')
        with raises(KeyError) as exc_info:
            actual_result = response.json()[key_pokemon_url]
            raise KeyError("key_pokemon_url must be pokemon")
        assert exc_info.type is KeyError




