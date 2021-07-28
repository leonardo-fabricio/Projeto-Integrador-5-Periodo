from django.urls import path
from django.urls.conf import re_path
from appsite.views import index
from django.views.generic.base import RedirectView
from django.conf.urls import url


urlpatterns = [
    path('', index),
]