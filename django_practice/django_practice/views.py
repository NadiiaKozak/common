from django.http import HttpResponse, Http404
from django.shortcuts import render

from .config import get_pockemon


def health_check(request):
    return HttpResponse('OK')


def index(request):
    return render(request, 'index.html')


def pokemons(request):
    latest_pokemon_list = [f"{p['pokemon']['name']}" for p in get_pockemon()['pokemon']]
    context = {'latest_pokemon_list': latest_pokemon_list}
    return render(request, 'pokemons.html', context)


def pokemon(request, pokemon):
    try:
        name_pokemon = [f"{p['pokemon']['name']}" for p in get_pockemon()['pokemon'] if
                                p['pokemon']['name'] == pokemon]
    except pokemon.DoesNotExist:
        raise Http404("Pokemon does not exist")
    return render(request, 'pokemon.html', {'pokemon': name_pokemon[0]})
