from django.shortcuts import render
from django.http import HttpResponseNotAllowed
from django.views.decorators.http import require_http_methods
from .models import Processo, Pagina
from datetime import date

@require_http_methods(["GET"])
def map(request):
    last_pagina = Pagina.objects.last()
    paginas = Pagina.objects.all()
    processos = Processo.objects.filter(pagina=last_pagina)
    s = get_statistic(processos)
    context = {
        'title': "Mapa de Improbidade",
        'processos': processos,
        'ano': last_pagina.ano,
        'pagina': last_pagina,
        'paginas': paginas,
        'total_sentencas': s['total'],
        'sentencas': s['sentencas'],
    }
    return render(request, 'map/mapa.html', context)

@require_http_methods(["GET"])
def map_by_year(request, year):
    paginas = Pagina.objects.all()
    try:
        pagina = paginas.get(ano=year)
    except Pagina.DoesNotExist:
        return HttpResponseNotAllowed('<h1>Page not found</h1>')
    processos = Processo.objects.filter(pagina=pagina)
    s = get_statistic(processos)
    context = {
        'title': "Mapa de Improbidade",
        'processos': processos,
        'ano': year,
        'pagina': pagina,
        'paginas': paginas,
        'total_sentencas': s['total'],
        'sentencas': s['sentencas'],
    }
    return render(request, 'map/mapa.html', context)

def get_statistic(processos):
    statistic = {}
    total = len(processos)
    statistic['total'] = total
    statistic['sentencas'] = {}
    for p in processos:
        if '/' in p.tipo_fundo:
            tipo = p.tipo_fundo.split('/')[0].strip(' ')
        elif '-' in p.tipo_fundo:
            tipo = p.tipo_fundo.split('-')[0].strip(' ')
        else:
            tipo = p.tipo_fundo
        try:
            statistic['sentencas'][tipo] += 1
        except KeyError:
            statistic['sentencas'][tipo] = 1
    
    for i in statistic['sentencas'].keys():
        statistic['sentencas'][i] = [statistic['sentencas'][i], (statistic['sentencas'][i]/total)*100]
    
    return statistic