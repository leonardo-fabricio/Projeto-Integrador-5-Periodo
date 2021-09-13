from django.contrib import admin
from .models import *

# Register your models here.
class EventsAdmin(admin.ModelAdmin):
    list_display = ['id','titulo','descricao','qtdPessoas', 'horaInicial', 'horaFinal', 'dataEvento', 'local','foto','id_estabelecimento']

class PublicoEventosAdmin(admin.ModelAdmin):
    list_display = ['id_publico', 'id_evento', 'qtdPessoas']

admin.site.register(Events, EventsAdmin)
admin.site.register(Publico_Eventos, PublicoEventosAdmin)