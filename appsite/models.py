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
    
class PublicoGeral(models.Model):
    nome = models.CharField('nome', max_length=100)
    telefone = models.CharField('telefone', max_length=50)
    cidade = models.CharField('cidade', max_length=100)
    email = models.CharField('email', max_length = 100, null=True)
    
class Eventos(models.Model):
    qtdPessoas = models.IntegerField('qtdPessoas')
    horaInicial = models.DateTimeField('horaInicial')
    horaFinal = models.DateTimeField('horaFinal')
    id_estabelecimento = models.ForeignKey('appsite.Estabelecimentos', on_delete = models.PROTECT)
    
class Publico_Eventos(models.Model):
    id_pessoa = models.ForeignKey('appsite.PublicoGeral', on_delete=models.PROTECT)
    id_evento = models.ForeignKey('appsite.Eventos', on_delete=models.PROTECT)