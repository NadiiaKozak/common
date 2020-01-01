from http import HTTPStatus

from django.test import Client
from django.test import TestCase
from django.urls import reverse
from pytest import raises

from .config import get_pockemon


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
        response = get_pockemon()
        assert isinstance(response, dict)

    def test_pokemons_key_error(self):
        key_pokemon_url = 'name'
        with raises(KeyError) as exc_info:
            actual_result = get_pockemon()[key_pokemon_url]
            raise KeyError("key_pokemon_url must be 'pokemon'")
        assert exc_info.type is KeyError




