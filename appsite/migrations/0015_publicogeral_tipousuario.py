# Generated by Django 3.2.4 on 2021-08-22 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0014_estabelecimentos_senha'),
    ]

    operations = [
        migrations.AddField(
            model_name='publicogeral',
            name='tipoUsuario',
            field=models.CharField(max_length=100, null=True, verbose_name='tipoUsuario'),
        ),
    ]
