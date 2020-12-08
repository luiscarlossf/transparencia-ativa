# Transparência Ativa
![Django CI](https://github.com/luiscarlossf/transparencia-ativa/workflows/Django%20CI/badge.svg)

O conceito de Transparência Ativa, nome do Projeto, está disposto no artigo 8º da Lei Nº 12.527, de 18 de novembro de 2011, a chamada Lei de Acesso à Informação (LAI).

O objetivo do projeto é apresentar dados de sentenças de improbidade expedidas no Piauí. O mapa mostra as cidades onde as sentenças foram proferidas, bem como informações sobre os processos. 

![Default Map View](screenshots/map.png?raw=true "Title")

# Começando

Primeiro clone o repositório do GitHub e mude para o novo diretório:

    $ git clone git@github.com/luiscarlossf/transparencia-ativa.git
    $ cd transparencia-ativa
    
Ative a virtualenv para o seu projeto.
    
Instale as dependências do projeto:

    $ pip install -r requirements.txt
    
    
Então, simplesmente aplique as migrações:

    $ python manage.py migrate
    

Você pode agora rodar o servidor de desenvolvimento:

    $ python manage.py runserver