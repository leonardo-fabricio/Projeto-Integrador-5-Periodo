# Generated by Django 3.2.4 on 2021-08-29 14:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0025_publico_eventos_qtdpessoasp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='publico_eventos',
            old_name='id_evento',
            new_name='idEvento',
        ),
        migrations.RenameField(
            model_name='publico_eventos',
            old_name='id_pessoa',
            new_name='idPessoa',
        ),
    ]
