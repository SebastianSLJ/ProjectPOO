from django.contrib import admin
from django.urls import include, path
from polls import views

# Patrones de urls
urlpatterns = [    
    path('admin/', admin.site.urls),  
    path('', include('polls.urls')),  # path de aplicacion (polls)
]
