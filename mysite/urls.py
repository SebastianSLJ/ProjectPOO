from django.contrib import admin
from django.urls import include, path
from polls import views

# Patrones de urls
urlpatterns = [    
    path('admin/', admin.site.urls),  
    path('empleos/', include('jobs.urls')), # path de pagina de empleos (job)
    path('', include('polls.urls')),  # path de aplicacion principal (polls)
    
]
