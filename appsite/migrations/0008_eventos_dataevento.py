# Generated by Django 3.2.4 on 2021-08-16 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0007_publicogeral_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventos',
            name='dataEvento',
            field=models.CharField(max_length=100, null=True, verbose_name='dataEvento'),
        ),
    ]
