from django.shortcuts import render
from django.http import HttpResponse


def home(request): #path home
    return render(request, "polls/index.html")

def registro(request): #path formulario
    return render(request, "polls/registro.html")

def sobre(request): #path aspirantes
    return render(request, "polls/about.html")

def empresas(request): #path empresas
    return render(request, "polls/principal_empresas.html")



