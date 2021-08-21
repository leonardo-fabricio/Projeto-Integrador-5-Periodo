from typing import Tuple
from django.db import models
from django.db.models.base import Model
from stdimage.models import StdImageField # serve para uso de campos com imagem

# Create your models here.
class Estabelecimentos(models.Model):
    nome = models.CharField('nome', max_length=100)
    tipo = models.CharField('tipo', max_length=100)
    rua = models.CharField('rua', max_length=100)
    cep = models.CharField('cep', max_length=100)
    cidade = models.CharField('cidade', max_length=100)
    email = models.EmailField('email', max_length=100, null=True)
    tipoUsuario = models.CharField('tipoUsuario', max_length=100, null=True)
    senha = models.CharField('senha',max_length=100,null=True)
    
class PublicoGeral(models.Model):
    nome = models.CharField('nome', max_length=100)
    telefone = models.CharField('telefone', max_length=50)
    cidade = models.CharField('cidade', max_length=100)
    email = models.CharField('email', max_length = 100, null=True)
    
class Eventos(models.Model):
    qtdPessoas  = models.IntegerField('qtdPessoas')
    dataEvento  = models.CharField('dataEvento', null= True, max_length=100)
    horaInicial = models.CharField('horaInicial',max_length=100)
    horaFinal   = models.CharField('horaFinal',max_length=100)
    local       = models.CharField('local', max_length=100, null=True)
    id_estabelecimento = models.ForeignKey('appsite.PublicoGeral', on_delete = models.PROTECT)
    # imagem             = models.StdImageField('Imagem', upload_to='imageEvents', variations={'thumb': (124,124)})
    
class Publico_Eventos(models.Model):
    id_pessoa = models.ForeignKey('appsite.PublicoGeral', on_delete=models.PROTECT)
    id_evento = models.ForeignKey('appsite.Eventos', on_delete=models.PROTECT)
    
class Gatilhos_users(models.Model):
    changed_column = models.CharField('changed_column', max_length=100)
    data_changed = models.DateTimeField('data_changed')
    old_value = models.CharField('old_value', max_length=100)
    new_value = models.CharField('new_value', max_length=100)
    operation = models.CharField('operation', max_length=100)