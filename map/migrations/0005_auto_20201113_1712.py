# Generated by Django 3.1.3 on 2020-11-13 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20201109_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='valor_multa',
            field=models.CharField(max_length=1500, verbose_name='Valor da Multa'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='valor_ressarcimento',
            field=models.CharField(max_length=1500, verbose_name='Valor de Ressarcimento'),
        ),
    ]
