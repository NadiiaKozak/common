import requests
from django.http import HttpResponse, Http404
from django.shortcuts import render

POCKEMON_URL = 'https://pokeapi.co/api/v2/'


def health_check(request):
    return HttpResponse('OK')


def index(request):
    return render(request, 'index.html')


def pokemons(request):
    response = requests.get(f'{POCKEMON_URL}/type/3')
    latest_pokemon_list = [f"{p['pokemon']['name']}" for p in response.json()['pokemon']]
    context = {'latest_pokemon_list': latest_pokemon_list}
    return render(request, 'pokemons.html', context)


def pokemon(request, pokemon):
    response = requests.get(f'{POCKEMON_URL}/type/3')
    try:
        name_pokemon = [f"{p['pokemon']['name']}" for p in response.json()['pokemon'] if
                                p['pokemon']['name'] == pokemon]
    except pokemon.DoesNotExist:
        raise Http404("Pokemon does not exist")
    return render(request, 'pokemon.html', {'pokemon': name_pokemon[0]})
