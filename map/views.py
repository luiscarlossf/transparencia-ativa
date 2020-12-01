from django.shortcuts import render
from django.http import HttpResponseNotAllowed, JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Processo, Pagina, Cidade
from datetime import date
import json

@require_http_methods(["GET"])
def map(request):
    '''
    Retorna os dados referente ao ano mais recente.
    '''
    pagina = Pagina.objects.last()
    
    if(pagina):
        paginas = Pagina.objects.all()
        processos = Processo.objects.filter(pagina=pagina)
        s = get_statistic(pagina)
        context = {
            'title': "Mapa de Improbidade",
            'processos': list(processos.values()),
            'ano': pagina.ano,
            'pagina': pagina,
            'paginas': list(paginas),
            'total_sentencas': s['total'],
            'sentencas': s['sentencas'],
        }
    else:
        context = {
            'title': "Mapa de Improbidade",
            'processos': None,
            'ano': None,
            'pagina': None,
            'paginas': None,
            'total_sentencas': None,
            'sentencas': None,
        }
    
    
    return render(request, 'map/mapa.html', context)

@require_http_methods(["GET"])
def map_json(request, year):
    '''
    Retorna um objeto JSON com os dados referente ao ano.
    '''
    paginas = Pagina.objects.all()
    try:
        pagina = paginas.get(ano=year)
    except Pagina.DoesNotExist:
        return HttpResponseNotAllowed('<h1>Page not found</h1>')
    cidades = Cidade.objects.all().values()
    saida = list()
    s = get_statistic(pagina)
    for cidade in cidades:
        cidade['processos'] = list(Processo.objects.filter(pagina=pagina, cidade__id=cidade['id']).values())
        if(len(cidade['processos']) != 0):
            saida.append(cidade)
    context = {
        'title': "Mapa de Improbidade",
        'cidades': saida,
        'ano': year,
        'sentencas': s['sentencas'],
    }
    return JsonResponse(context, safe=True)

@require_http_methods(["GET"])
def map_by_year(request, year):
    '''
    Retorna dos dados referentes ao ano(year) requisitiado.
    '''
    paginas = Pagina.objects.all()
    try:
        pagina = paginas.get(ano=year)
    except Pagina.DoesNotExist:
        return HttpResponseNotAllowed('<h1>Page not found</h1>')
    processos = Processo.objects.filter(pagina=pagina)
    s = get_statistic(pagina)
    context = {
        'title': "Mapa de Improbidade",
        'processos': list(processos.values()),
        'ano': year,
        'pagina': pagina,
        'paginas': list(paginas),
        'total_sentencas': s['total'],
        'sentencas': s['sentencas'],
    }
    return render(request, 'map/mapa.html', context)

def get_statistic(pagina):
    '''
    Retorna dados estatísticos dos processos. 
    Quantidade de sentenças por temática.
    '''
    processos = Processo.objects.filter(pagina=pagina)
    statistic = {}
    total = len(processos)
    statistic['total'] = total
    statistic['sentencas'] = {}
    for p in processos:
        if '/' in p.tipo_fundo:
            tipo = p.tipo_fundo.split('/')[0].strip(' ')
        elif '-' in p.tipo_fundo:
            tipo = p.tipo_fundo.split('-')[0].strip(' ')
        elif '(' in p.tipo_fundo:
            tipo = p.tipo_fundo.split('(')[0].strip(' ')
        else:
            tipo = p.tipo_fundo
        try:
            statistic['sentencas'][tipo] += 1
        except KeyError:
            statistic['sentencas'][tipo] = 1
    
    for i in statistic['sentencas'].keys():
        statistic['sentencas'][i] = [statistic['sentencas'][i], (statistic['sentencas'][i]/total)*100]
    
    return statistic