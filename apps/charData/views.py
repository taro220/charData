from django.shortcuts import render
from .models import Players, Characters
from django.core import serializers
from django.http import HttpResponse, JsonResponse
import json

# Create your views here.
def index(request):
    Players.objects.all().delete()
    Characters.objects.all().delete()
    Players.objects.create(name = "Phill", gold = 100)
    Characters.objects.create(char_class = "Warrior", char_level = 50, maxHealth = 75)
    content = {
    'player_list' : Players.objects.all(),
    'char_list' : Characters.objects.all()
    }

    return render(request, "charData/index.html", content)


def char_json(request):
    print "Database hit"
    player = Players.objects.all()
    data_list = list(player.values('name','gold'))
    return JsonResponse(data_list, safe=False)
