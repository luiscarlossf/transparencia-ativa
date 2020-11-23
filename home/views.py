from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def index(request):
    context = {
        'title': "Início",
    }
    return render(request, 'home/index.html', context)
