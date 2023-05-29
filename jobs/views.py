from django.shortcuts import render
from jobs.models import Post


def empleos(request): #path empleos
    posts = Post.objects.all()
    return render(request, "jobs/empleos.html", {"posts": posts})
