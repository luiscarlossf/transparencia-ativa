from django.urls import path
from . import views

urlpatterns = [
    path('mapa.html', views.map),
]
