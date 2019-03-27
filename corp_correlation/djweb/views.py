from django.shortcuts import render
from .models import User, Other
from django.db.models import Q


def index(request):
    return render("index.html")


def add_client(request):
    in_other = Other.object.filter(name__iexact=request.GET["name"])
    if len(in_other) != 0:
        other = in_other[0]
        new_user = User(name=other.name,
                        description=other.description,
                        competitors=other.competitors,
                        has_clients=other.has_clients,
                        client_of=other.client_of)
        new_user.save()
    return ""


def add_relation(request):
    return ""


def check_relation(request):
    return ""
