from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=200,null=False,blank=False, unique=True, verbose_name="Nome")
    longitude = models.FloatField(verbose_name="Longitude")
    latitude = models.FloatField(verbose_name="Latitude")

class Pagina(models.Model):
    texto = models.TextField(verbose_name="Texto da página", help_text="Artigo presente abaixo do mapa das sentenças de improbidades.")
    ano = models.IntegerField(verbose_name="Ano", help_text="Entre com o ano em que os dados da página foram coletados.")

class Processo(models.Model):
    numero = models.CharField(verbose_name="Número do processo", max_length=100)
    resumo = models.TextField(verbose_name="Resumo")
    valor_ressarcimento = models.FloatField(verbose_name="Valor de Ressarcimento")
    valor_multa = models.FloatField(verbose_name="Valor da Multa")
    cidade = models.ForeignKey(Cidade, verbose_name="Cidade", on_delete=models.SET_NULL, null=True, blank=True)
    pagina = models.ForeignKey(Pagina, verbose_name="Página", on_delete=models.SET_NULL, null=True, blank=True)

class Estatistica(models.Model):
    pagina = models.ForeignKey(Pagina, verbose_name="Página", on_delete=models.CASCADE)
    total_sentencas = models.IntegerField(verbose_name="Total de sentenças")    
    total_educacao = models.IntegerField(verbose_name="Quantidade em Educação")
    total_saude = models.IntegerField(verbose_name="Quantidade em Saúde")
    total_infraestrutura = models.IntegerField(verbose_name="Quantidade em Infraestrutura")
    total_seguridade_social = models.IntegerField(verbose_name="Quantidade em Seguridade Social")
    total_outros = models.IntegerField(verbose_name="Quantidade em Outras áreas")
    total_assistencia_social = models.IntegerField(verbose_name="Quantidade em Assistência Social")
    total_habitacao = models.IntegerField(verbose_name="Quantidade em Habitação")
    total_reforma_agraria = models.IntegerField(verbose_name="Quantidade em Reforma Agrária")
    total_turismo = models.IntegerField(verbose_name="Quantidade em Turismo")