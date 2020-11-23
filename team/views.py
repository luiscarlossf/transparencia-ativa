from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def team(request):
    context= {
        'title': "Equipe",
    }
    return render(request, 'team/equipe.html', context)
