# Generated by Django 3.2.6 on 2021-09-12 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsiteCrudEventos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publico_Eventos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_publico', models.IntegerField()),
                ('id_evento', models.IntegerField()),
                ('qtdPessoas', models.IntegerField()),
            ],
        ),
    ]
