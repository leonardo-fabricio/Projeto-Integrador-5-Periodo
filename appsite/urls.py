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
    path('login', login, name='login'),
    path('profile', profile),
    path('dashboard', dashboard),
    
    path('accounts/', include('allauth.urls')),
    path('sair/', LogoutView.as_view() , name='sair'),
    path('cadastroEstabelecimento/<str:email>', cadastroEstabelecimento, name='cadastroEstabelecimento'),
    path('cadastroPublico/<str:email>', cadastroPublico, name='cadastroPublico'),
]