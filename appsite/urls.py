from django.urls import path
from django.urls.conf import re_path
from appsite.views import * # importar tudo para evitar erros
from django.views.generic.base import RedirectView
from django.conf.urls import url


urlpatterns = [
    path('', index, name='index'),
    path('login', login, name='login')
    # path('teste', teste, name='teste')
]