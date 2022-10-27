from datetime import datetime
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from team.forms import TeamForm
from team.models import Team

def get_teams(request):
    teams = Team.objects.all()
    #paginator = Paginator(courses, 3)
    #page_number = request.GET.get("page")
    #return paginator.get_page(page_number)
    return teams

def create_team(request):
    if request.method == "POST":
        team_form = TeamForm(request.POST)
        if team_form.is_valid():
            data = team_form.cleaned_data
            actual_objects = Team.objects.filter(
                city=data["city"], name=data["name"]
            ).count()
            print("actual_objects", actual_objects)
            if actual_objects:
                messages.error(
                    request,
                    f"El equipo de {data['name']} ya esta en la BD",
                )
            else:
                team = Team(
                    city=data["city"],
                    name=data["name"], 
                    owner=data["owner"],
                    found_in=data["found_in"],
                    )
                team.save()
                messages.success(
                    request,
                    f"{data['city']} {data['name']} ha sido creado exitosamente!",
                )

            return render(
                request=request,
                context={"teams": get_teams(request)},
                template_name="team/team_list.html",
            )

    team_form = TeamForm(request.POST)
    context_dict = {"form": team_form}
    return render(
        request=request,
        context=context_dict,
        template_name="team/team_form.html",
    )


def teams(request):
    #teams = Team.objects.all()
    #context_dict = {"teams": teams}
    return render(
        request=request,
        context={"teams": get_teams(request)}, #context_dict,
        template_name="team/team_list.html",
    )