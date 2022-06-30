from django.contrib import admin
from rede_social.models import Pessoa, Postagem, Comentario, MensagemDeContato

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    list_display = ('id', 'nome')
    list_display_links = list_display
    list_per_page = 10
    list_filter = ('id','nome')

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'data')
    list_display_links = list_display
    list_per_page = 10
    list_filter = ('id','pessoa', 'data')

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('id', 'pessoa', 'data')
    list_display_links = list_display
    list_per_page = 10
    list_filter = ('id','pessoa','data')

@admin.register(MensagemDeContato)
class MensagemDeContatoAdmin(admin.ModelAdmin):
    list_display = ('id','nome', 'email')
    list_display_links = list_display
    readonly_fields = ('data', )
    list_per_page = 10
    list_filter = ('id','email')

