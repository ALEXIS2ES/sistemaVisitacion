from django.urls import path
from .views import crearVisita

urlpatterns = [
	path('crear_visita/', crearVisita, name = 'crear_visita')
]