from django.contrib.auth import logout
from django.urls import path, include
from django.urls.conf import re_path
from appsite.views import * # importar tudo para evitar erros
from django.views.generic.base import RedirectView
from django.conf.urls import url

from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView, logout_then_login


urlpatterns = [
    path('', index, name='index'),
    path('profile', profile),
    path('dashboard/eventosDisponiveis', dashboard, name='eventosDisponiveis'),
    
    path('accounts/', include('allauth.urls')),
    path('sair/', LogoutView.as_view() , name='sair'),
    path('cadastroEstabelecimento', cadastroEstabelecimento, name='cadastroEstabelecimento'),
    path('cadastroPublico', cadastroPublico, name='cadastroPublico'),
   
    path('dashboard/suasReservas', suasReservas, name='suasReservas'),
    path('escolha', escolha, name='escolha'),
   
    path('informacoesEventos/<int:idauxiliar>',informacoesEventos, name='informacoesEventos' ),
    path('baixarPdf/<int:idauxiliar>',baixarPdf, name='baixarPdf'),
    
    path('criarEvento', criarEvento, name='criarEvento'),
    path('deleteEventos/<int:idauxiliar>/', deleteEventos, name='deleteEventos'),
    
    path('publicoEventos/<int:idauxiliar>/<int:idpublico>/', Publico_eventos, name='publicoEventos'),
    
    path('deletePublicoEventos/<int:idauxiliar>/<int:idpublico>', deletePublicoEventos, name='deletePublicoEventos'),
    path('editar_evento/<int:idauxiliar>/', EditarEvento, name='editar_evento'),
    
    path('dashboard_admin', GatilhosListView.as_view(), name='dashboard_admin'),    
  
]