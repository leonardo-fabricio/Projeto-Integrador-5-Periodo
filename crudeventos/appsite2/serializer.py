from .models import *
from rest_framework import serializers

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eventos
        fields = ['titulo','descricao','qtdPessoas', 'horaInicial', 'horaFinal', 'dataEvento', 'local','foto']