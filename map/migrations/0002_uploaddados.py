# Generated by Django 3.1.3 on 2020-11-09 19:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UploadDados',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(help_text='Envie o arquivo no formato especificado neste <a href="https://drive.google.com/file/d/1Y_yQAKVMWj5e42_Bawun3-y1nsyIJ-oD/view?usp=sharing">link</a>. Não altere os campos, nem adicione estilização ao documento!', upload_to='uploads/%Y/', verbose_name='Arquivo CSV')),
                ('pagina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='map.pagina', verbose_name='Página')),
            ],
        ),
    ]
