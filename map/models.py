from django.db import models
import csv
from django.db.models.signals import post_save
from django.dispatch import receiver

class Cidade(models.Model):
    nome = models.CharField(max_length=200,null=False,blank=False, unique=True, verbose_name="Nome")
    longitude = models.FloatField(verbose_name="Longitude")
    latitude = models.FloatField(verbose_name="Latitude")
    
    def __str__(self):
        """
        String representanda a cidade.
        """
        return self.nome

class Pagina(models.Model):
    texto = models.TextField(verbose_name="Texto da página", help_text="Artigo presente abaixo do mapa das sentenças de improbidades.")
    ano = models.IntegerField(verbose_name="Ano", help_text="Entre com o ano em que os dados da página foram coletados.")
    
    def __str__(self):
        """
        String representanda a página.
        """
        return str(self.ano)

class Processo(models.Model):
    numero = models.CharField(verbose_name="Número do processo", max_length=100)
    resumo = models.TextField(verbose_name="Resumo")
    tipo_fundo = models.CharField(verbose_name="Tipo do fundo", max_length=200, null=True)
    valor_ressarcimento = models.CharField(verbose_name="Valor de Ressarcimento", max_length=1500)
    valor_multa = models.CharField(verbose_name="Valor da Multa", max_length=1500)
    cidade = models.ForeignKey(Cidade, verbose_name="Cidade", on_delete=models.SET_NULL, null=True, blank=True)
    pagina = models.ForeignKey(Pagina, verbose_name="Página", on_delete=models.SET_NULL, null=True, blank=True)
    
    def __str__(self):
        """
        String representanda o processo.
        """
        return str(self.numero)

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
    def __str__(self):
        """
        String representanda a estatística.
        """
        return str(self.pagina.ano) +'-'+ str(self.total_sentencas)

def data_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'uploads/{0}/{1}'.format(instance.pagina.ano, filename)

class UploadDados(models.Model):
    pagina = models.ForeignKey(Pagina, verbose_name="Página", on_delete=models.CASCADE)
    arquivo = models.FileField(verbose_name="Arquivo CSV", upload_to=data_directory_path, help_text='Envie o arquivo no formato especificado neste <a href="https://drive.google.com/file/d/1Y_yQAKVMWj5e42_Bawun3-y1nsyIJ-oD/view?usp=sharing" target="_blank">link</a>. Não altere os campos, nem adicione estilização ao documento!')

    def __str__(self):
        """
        String representanda a estatística.
        """
        return str(self.pagina.ano)

        
@receiver(post_save, sender=UploadDados, weak=False, dispatch_uid='convert_csv')
def from_csv_to_db(sender, instance, **kwargs):
    filename = instance.arquivo.name
    print("Convertendo CSV")
    with open(filename, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(row)