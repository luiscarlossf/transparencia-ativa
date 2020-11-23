from django.shortcuts import render
from django.views.decorators.http import require_http_methods

@require_http_methods(["GET"])
def note(request):
    context = {
        'title': "Apontamentos",
    }
    
    return render(request, 'note/achados.html', context)
