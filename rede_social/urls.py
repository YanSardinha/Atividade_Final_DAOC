from django.urls import path
from rede_social.views import ContatoSucessoView, ContatoView, index, perfil_template, PostagemView, seguir, desseguir, PostDetalhado

urlpatterns = [
    path('', index, name="index"),
    path('contato/', ContatoView.as_view(), name='form_contato'),
    path('contato_sucesso/', ContatoSucessoView.as_view(), name='contato_sucesso'),
    path('postagem/', PostagemView.as_view(), name='postagem'),
    path('postagem/<int:pk>', PostDetalhado.as_view(), name='postagem-detalhe'),
    path('<str:slug>', perfil_template, name='perfil'),
    path('<str:slug>/follow', seguir, name='follow'),
    path('<str:slug>/unfollow', desseguir, name='unfollow'),
]
