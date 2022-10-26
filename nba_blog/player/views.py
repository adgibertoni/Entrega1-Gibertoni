from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from player.forms import PlayerForm
from player.models import Player


def get_players(request):
    players = Player.objects.all()
    #paginator = Paginator(courses, 3)
    #page_number = request.GET.get("page")
    #return paginator.get_page(page_number)
    return players

def create_player(request):
    if request.method == "POST":
        player_form = PlayerForm(request.POST)
        if player_form.is_valid():
            data = player_form.cleaned_data
            actual_objects = Player.objects.filter(
                name=data["name"], last_name=data["last_name"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El jugador {data['name']} {data['last_name']} ya fue creado",
                )
            else:
                player = Player(
                    name=data["name"], 
                    last_name=data["last_name"],
                    country=data["country"],
                    number=data["number"],
                    points=data["points"]
                    )
                player.save()
                messages.success(
                    request,
                    f"Jugador {data['name']} {data['last_name']} creado exitosamente!",
                )

            return render(
                request=request,
                context={"players": get_players(request)},
                template_name="player/player_list.html",
            )

    player_form = PlayerForm(request.POST)
    context_dict = {"form": player_form}
    return render(
        request=request,
        context=context_dict,
        template_name="player/player_form.html",
    )


def players(request):
    #players = Player.objects.all()
    #context_dict = {"players": players}
    return render(
        request=request,
        context={"players": get_players(request)}, #context_dict,
        template_name="player/player_list.html",
    )