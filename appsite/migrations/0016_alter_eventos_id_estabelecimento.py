# Generated by Django 3.2.4 on 2021-08-22 18:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0015_publicogeral_tipousuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='id_estabelecimento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='appsite.estabelecimentos'),
        ),
    ]
