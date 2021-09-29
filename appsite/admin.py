from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Estabelecimentos)
admin.site.register(PublicoGeral)
admin.site.register(Gatilhos_users)
