from django.contrib import admin

from .models import Ecfgusuario

# Configuração do DjangoAdmin

@admin.register(Ecfgusuario)
class EcfgusuarioAdmin(admin.ModelAdmin):
    list_display = ('delogin', 'nmusuario')
