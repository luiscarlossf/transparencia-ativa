from django.urls import path
from . import views

urlpatterns = [
    path('eventos-turminha.html', views.events),
]