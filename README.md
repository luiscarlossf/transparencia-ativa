# Transparência Ativa
![Django CI](https://github.com/luiscarlossf/transparencia-ativa/workflows/Django%20CI/badge.svg)

O conceito de Transparência Ativa, nome do Projeto, está disposto no artigo 8º da Lei Nº 12.527, de 18 de novembro de 2011, a chamada Lei de Acesso à Informação (LAI).


{% if False %}

# Introdução

O objetivo do projeto é apresentar dados de sentenças de improbidade expedidas no Piauí. O mapa mostra as cidades onde as sentenças foram proferidas, bem como informações sobre os processos. 

![Default Map View](screenshots/map.png?raw=true "Title")

# Uso

Para testar o sistema realize

### Existing virtualenv

If your project is already in an existing python3 virtualenv first install django by running

    $ pip install django
    
And then run the `django-admin.py` command to start the new project:

    $ django-admin.py startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
### No virtualenv

This assumes that `python3` is linked to valid installation of python 3 and that `pip` is installed and `pip3`is valid
for installing python 3 packages.

Installing inside virtualenv is recommended, however you can start your project without virtualenv too.

If you don't have django installed for python 3 then run:

    $ pip3 install django
    
And then:

    $ python3 -m django startproject \
      --template=https://github.com/nikola-k/django-template/zipball/master \
      --extension=py,md \
      <project_name>
      
      
After that just install the local dependencies, run migrations, and start the server.

{% endif %}

# {{ project_name|title }}

# Começando

Primeiro clone o repositório do GitHub e mude para o novo diretório:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Ative a virtualenv para o seu projeto.
    
Instale as dependências do projeto:

    $ pip install -r requirements.txt
    
    
Então, simplesmente aplique as migrações:

    $ python manage.py migrate
    

Você pode agora rodar o servidor de desenvolvimento:

    $ python manage.py runserver