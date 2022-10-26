from django.urls import path

from player import views

app_name = "player"
urlpatterns = [
    path("player", views.players, name="player-list"),
    path("player/add", views.create_player, name="player-add"),
]
