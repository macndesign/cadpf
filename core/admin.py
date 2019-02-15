from django.contrib import admin
from core.models import Cadastro


class CadastroAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_nascimento', 'genero')
    list_filter = ('nome',)

admin.site.register(Cadastro, CadastroAdmin)
