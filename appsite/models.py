from django.db import models
from django.db.models.base import Model

# Create your models here.
class Estabelecimentos(models.Model):
    nome = models.CharField('nome', max_length=100)
    tipo = models.CharField('tipo', max_length=100)
    rua = models.CharField('rua', max_length=100)
    cep = models.CharField('cep', max_length=100)
    cidade = models.CharField('cidade', max_length=100)
    email = models.EmailField('email', max_length=100, null=True)
