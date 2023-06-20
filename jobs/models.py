from django.db import models
from django.contrib.auth.models import User

class Categorias(models.Model):
    nombre = models.CharField(max_length=50)     
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nombre

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    contenido = models.CharField(max_length=100)
    autor = models.CharField(max_length=50)
    ubicacion = models.CharField(max_length=20)
    image = models.ImageField(upload_to="media", null=True, blank=True)    
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    categorias = models.ManyToManyField(Categorias)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = 'empleo'
        verbose_name_plural = 'empleos'
