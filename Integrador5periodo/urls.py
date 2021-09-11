"""Integrador5periodo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from pathlib import Path
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
from django.urls.conf import include
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from appsite.views import *

router = routers.DefaultRouter()
router.register(r'api-publico', PublicoViewSet)
router.register(r'api-estabelecimento', EstabelecimentoViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('appsite.urls')),# 
    path(r'accounts/', include('django.contrib.auth.urls')),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),

    path('', include('social_django.urls'), name='social'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
