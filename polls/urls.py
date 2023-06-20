from django.urls import path 
from polls import views 


# Patrones de url (apliacion)
urlpatterns = [   
    path('', views.home, name="Home"),
    path('registro/', views.registro, name="Registro"), 
    path('about/', views.sobre, name="Sobre"), 
    path('empresas/', views.empresas, name="Empresas"), 
] 