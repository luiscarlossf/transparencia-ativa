from django.urls import path
from . import views

urlpatterns = [
    path('achados.html', views.note),
]