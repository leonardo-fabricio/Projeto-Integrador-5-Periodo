# Generated by Django 3.2.4 on 2021-09-02 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsite', '0032_auto_20210902_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventos',
            name='titulo',
            field=models.CharField(max_length=25, null=True, verbose_name='titulo'),
        ),
    ]
