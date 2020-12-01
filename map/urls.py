from django.urls import path
from . import views

urlpatterns = [
    path('mapa.html', views.map),
    path('mapa.html/<int:year>/', views.map_by_year),
    path('mapa.html/info/<int:year>/', views.map_json),
]
