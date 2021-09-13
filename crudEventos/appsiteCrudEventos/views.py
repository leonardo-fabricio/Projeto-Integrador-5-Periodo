from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializer import *


# Create your views here.
class EventoViewSet(viewsets.ModelViewSet):
    queryset = Events.objects.all()
    serializer_class = EventoSerializer

class PublicoEventoViewSet(viewsets.ModelViewSet):
    queryset = Publico_Eventos.objects.all()
    serializer_class = PublicoEventoSerializer
    