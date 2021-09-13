from .models import *
from rest_framework import serializers

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Events
        fields = ['id','titulo','descricao','qtdPessoas', 'horaInicial', 'horaFinal', 'dataEvento', 'local','foto','id_estabelecimento']

class PublicoEventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Publico_Eventos
        fields = ['id','id_evento','id_publico','qtdPessoas']