from django.contrib import admin

# Register your models here.
from .models import Estabelecimentos, Publico_Eventos, PublicoGeral, Eventos

admin.site.register(Estabelecimentos)
admin.site.register(PublicoGeral)
admin.site.register(Publico_Eventos)
admin.site.register(Eventos)