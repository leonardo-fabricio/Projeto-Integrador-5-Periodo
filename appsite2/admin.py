from django.contrib import admin
from .models import *
# Register your models here.

class EventosAdmin(admin.ModelAdmin):
    list_display = ['id','titulo','descricao','qtdPessoas', 'horaInicial', 'horaFinal', 'dataEvento', 'local','foto']
    
admin.site.register(Publico_Eventos)
admin.site.register(Eventos, EventosAdmin)