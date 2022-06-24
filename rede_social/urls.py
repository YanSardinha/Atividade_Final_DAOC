from django.urls import path
from rede_social.views import ContatoSucessoView, ContatoView, index, perfil_template, MensagemView

urlpatterns = [
    path('', index, name="index"),
    path('<str:slug>/', perfil_template, name='perfil'),
    path('contato/', ContatoView.as_view(), name='form_contato'),
    path('contato_sucesso/', ContatoSucessoView.as_view(), name='contato_sucesso'),
    path('mensagem/', MensagemView.as_view(), name='mensagem'),
]
