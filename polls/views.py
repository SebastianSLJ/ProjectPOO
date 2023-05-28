from django.shortcuts import render
from django.http import HttpResponse


def home(request): #path home
    return render(request, "polls/home.html")

def registro(request): #path encuesta
    return render(request, "polls/registro.html")

