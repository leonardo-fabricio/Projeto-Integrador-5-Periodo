from .models import *
from rest_framework import serializers

class EventoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Eventos
        fields = '__all__'