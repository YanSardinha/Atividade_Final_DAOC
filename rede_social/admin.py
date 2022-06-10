from django.contrib import admin
from rede_social.models import Pessoa, Postagem, Comentario, MensagemDeContato


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    exclude = ('slug',)
    pass

@admin.register(Postagem)
class PostagemAdmin(admin.ModelAdmin):
    pass

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    pass

@admin.register(MensagemDeContato)
class MensagemDeContatoAdmin(admin.ModelAdmin):
    readonly_fields = ('data', )
