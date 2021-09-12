from django.conf.urls import include
from django.urls import path
from .views import *

urlpatterns = [
    path('criarEvento', criarEvento, name='criarEvento'),
    path('deleteEventos/<int:id>', deleteEventos, name='deleteEventos'),
    path('publicoEventos/<int:idevento>/<int:idpublico>', Publico_eventos, name='publicoEventos'),
    path('deletePublicoEventos/<int:idevento>/<int:idpublico>', deletePublicoEventos,name='deletePublicoEventos'),
    path('editar_evento/<int:pk>/', EditarEventoView.as_view(), name='editar_evento'),
    path('',include('appsite.urls')),
]