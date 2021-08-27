from rest_framework import serializers
from appsite.models import *

class PublicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublicoGeral
        fields = '__all__'
        
class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eventos
        fields = ['titulo','descricao','qtdPessoas', 'horaInicial', 'horaFinal', 'dataEvento', 'local','foto']
        
        
class EstabelecimentoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Estabelecimentos
        fields = '__all__'