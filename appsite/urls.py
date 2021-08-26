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
    path('criarEvento', criarEvento, name='criarEvento'),
    path('dashboard/suasReservas', suasReservas, name='suasReservas'),
    path('escolha', escolha, name='escolha'),
    path('deleteEventos/<int:id>', deleteEventos, name='deleteEventos'),
]