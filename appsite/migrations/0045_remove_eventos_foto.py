# Generated by Django 3.2.6 on 2021-09-15 17:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0044_alter_eventos_foto'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventos',
            name='foto',
        ),
    ]
