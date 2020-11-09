# Generated by Django 3.1.3 on 2020-11-09 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cidade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, unique=True, verbose_name='Nome')),
                ('longitude', models.FloatField(verbose_name='Longitude')),
                ('latitude', models.FloatField(verbose_name='Latitude')),
            ],
        ),
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('texto', models.TextField(help_text='Artigo presente abaixo do mapa das sentenças de improbidades.', verbose_name='Texto da página')),
                ('ano', models.IntegerField(help_text='Entre com o ano em que os dados da página foram coletados.', verbose_name='Ano')),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=100, verbose_name='Número do processo')),
                ('resumo', models.TextField(verbose_name='Resumo')),
                ('valor_ressarcimento', models.FloatField(verbose_name='Valor de Ressarcimento')),
                ('valor_multa', models.FloatField(verbose_name='Valor da Multa')),
                ('cidade', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.cidade', verbose_name='Cidade')),
                ('pagina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='map.pagina', verbose_name='Página')),
            ],
        ),
        migrations.CreateModel(
            name='Estatistica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_sentencas', models.IntegerField(verbose_name='Total de sentenças')),
                ('total_educacao', models.IntegerField(verbose_name='Quantidade em Educação')),
                ('total_saude', models.IntegerField(verbose_name='Quantidade em Saúde')),
                ('total_infraestrutura', models.IntegerField(verbose_name='Quantidade em Infraestrutura')),
                ('total_seguridade_social', models.IntegerField(verbose_name='Quantidade em Seguridade Social')),
                ('total_outros', models.IntegerField(verbose_name='Quantidade em Outras áreas')),
                ('total_assistencia_social', models.IntegerField(verbose_name='Quantidade em Assistência Social')),
                ('total_habitacao', models.IntegerField(verbose_name='Quantidade em Habitação')),
                ('total_reforma_agraria', models.IntegerField(verbose_name='Quantidade em Reforma Agrária')),
                ('total_turismo', models.IntegerField(verbose_name='Quantidade em Turismo')),
                ('pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.pagina', verbose_name='Página')),
            ],
        ),
    ]
