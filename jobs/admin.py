from django.contrib import admin
from .models import Categorias, Post

class Categorias_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class Post_admin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categorias, Categorias_admin)
admin.site.register(Post, Post_admin)



