from django.contrib import admin

# Register your models here.
from .models import Estabelecimentos, Publico_Eventos, PublicoGeral, Eventos

class EventosAdmin(admin.ModelAdmin):
    list_display = ['id','titulo','descricao','qtdPessoas', 'horaInicial', 'horaFinal', 'dataEvento', 'local','foto']

admin.site.register(Estabelecimentos)
admin.site.register(PublicoGeral)
admin.site.register(Publico_Eventos)
admin.site.register(Eventos, EventosAdmin)