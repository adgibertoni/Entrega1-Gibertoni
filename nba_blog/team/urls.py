from django.urls import path

from team import views

app_name = "team"
urlpatterns = [
    path("team", views.teams, name="team-list"),
    path("team/add", views.create_team, name="team-add"),
]