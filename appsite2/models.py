from django.db import models

# Create your models here.
class Eventos(models.Model):
    titulo      = models.CharField('titulo', null= True, max_length=30)
    descricao   = models.CharField('descricao', null= True, max_length=100)
    qtdPessoas  = models.IntegerField('qtdPessoas')
    dataEvento  = models.CharField('dataEvento', null= True, max_length=100)
    horaInicial = models.CharField('horaInicial',max_length=100)
    horaFinal   = models.CharField('horaFinal',max_length=100)
    local       = models.CharField('local', max_length=100, null=True)
    id_estabelecimento = models.ForeignKey('appsite.Estabelecimentos', on_delete = models.CASCADE, null=True)
    foto      = models.FileField(upload_to="img/%Y/%m/%d", null=True)
    
class Publico_Eventos(models.Model):
    qtdPessoasP = models.IntegerField('qtdPessoas', null=True)
    idPessoa = models.ForeignKey('appsite.PublicoGeral', on_delete=models.CASCADE)
    idEvento = models.ForeignKey('appsite2.Eventos', on_delete=models.CASCADE)