# Generated by Django 3.1.3 on 2020-11-26 00:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0006_processo_tipo_fundo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagina',
            name='texto',
        ),
        migrations.DeleteModel(
            name='Estatistica',
        ),
    ]
