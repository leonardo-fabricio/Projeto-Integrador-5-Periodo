from rest_framework import serializers
from appsite.models import PublicoGeral

class PublicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PublicoGeral
        fields = '__all__'