# Generated by Django 3.2.4 on 2021-08-03 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0003_remove_estabelecimentos_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='estabelecimentos',
            name='email',
            field=models.EmailField(max_length=100, null=True, verbose_name='email'),
        ),
    ]
