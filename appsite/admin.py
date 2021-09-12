from django.contrib import admin

# Register your models here.
from .models import Estabelecimentos, PublicoGeral

admin.site.register(Estabelecimentos)
admin.site.register(PublicoGeral)
