from django.contrib import admin
from .models import Cidade, Estatistica, Pagina, Processo, UploadDados

admin.site.register(Cidade)
admin.site.register(Estatistica)
admin.site.register(Pagina)
admin.site.register(Processo)
admin.site.register(UploadDados)
