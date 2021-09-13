from django.db import models

# Create your models here.
class Events(models.Model):
    id          = models.AutoField(primary_key=True)
    titulo      = models.CharField('titulo', null= True, max_length=30)
    descricao   = models.CharField('descricao', null= True, max_length=100)
    qtdPessoas  = models.IntegerField('qtdPessoas')
    dataEvento  = models.CharField('dataEvento', null= True, max_length=100)
    horaInicial = models.CharField('horaInicial',max_length=100)
    horaFinal   = models.CharField('horaFinal',max_length=100)
    local       = models.CharField('local', max_length=100, null=True)
    foto      = models.FileField(upload_to="img/%Y/%m/%d", null=True)
    id_estabelecimento = models.IntegerField(null=True)
    
class Publico_Eventos(models.Model):
    id_publico = models.IntegerField()
    id_evento = models.IntegerField()
    qtdPessoas = models.IntegerField()