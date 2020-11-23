from django.urls import path
from . import views

urlpatterns = [
    path('equipe.html', views.team),
]