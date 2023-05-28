from django.shortcuts import render
from jobs.models import Post

def Empleos(request): #path empleos
    posts = Post.objects.all()
    return render(request, "job/empleos.html", {"posts", posts})