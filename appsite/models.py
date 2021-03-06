from typing import Tuple
from django.db import models
from django.db.models.base import Model
from django.forms.widgets import ClearableFileInput
from stdimage.models import StdImageField # serve para uso de campos com imagem


# Create your models here.
class Estabelecimentos(models.Model):
    nome = models.CharField('nome', max_length=100)
    tipo = models.CharField('tipo', max_length=100)
    email = models.EmailField('email', max_length=100, null=True, unique=True)
    tipoUsuario = models.CharField('tipoUsuario', max_length=100, null=True)
    foto      = models.FileField(upload_to="imgUser/%Y/%m/%d", null=True)

    
class PublicoGeral(models.Model):
    nome = models.CharField('nome', max_length=100)
    telefone = models.CharField('telefone', max_length=20)
    cidade = models.CharField('cidade', max_length=100)
    email = models.CharField('email', max_length = 100, null=True, unique=True)
    tipoUsuario = models.CharField('tipoUsuario', max_length=100, null=True)
    foto      = models.FileField(upload_to="imgUser/%Y/%m/%d", null=True)
    
class Eventos(models.Model):
    titulo      = models.CharField('titulo', null= True, max_length=30)
    descricao   = models.CharField('descricao', null= True, max_length=100)
    qtdPessoas  = models.IntegerField('qtdPessoas')
    dataEvento  = models.CharField('dataEvento', null= True, max_length=100)
    horaInicial = models.CharField('horaInicial',max_length=100)
    horaFinal   = models.CharField('horaFinal',max_length=100)
    local       = models.CharField('local', max_length=100, null=True) 
    
class Gatilhos_users(models.Model):
    changed_column = models.CharField('changed_column', max_length=100)
    data_changed = models.DateTimeField('data_changed')
    old_value = models.CharField('old_value', max_length=100)
    new_value = models.CharField('new_value', max_length=100)
    operation = models.CharField('operation', max_length=100)