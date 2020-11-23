from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def events(request):
    context = {
        'title': "Eventos",
    }
    return render(request, 'events/eventos-turminha.html', context)
