from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def map(request):
    context = {
        'title': "Mapa de Improbidade",
    }
    return render(request, 'map/mapa.html', context)
