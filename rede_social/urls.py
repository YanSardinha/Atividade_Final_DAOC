from django.urls import path
from rede_social.views import ContatoSucessoView, ContatoView, index, perfil_template, PostagemView, follow, unfollow, PostDetalhado

urlpatterns = [
    path('', index, name="index"),
    path('contato/', ContatoView.as_view(), name='form_contato'),
    path('contato_sucesso/', ContatoSucessoView.as_view(), name='contato_sucesso'),
    path('postagem/', PostagemView.as_view(), name='postagem'),
    path('postagem/<int:pk>', PostDetalhado.as_view(), name='postagem-detalhe'),
    path('<str:slug>/', perfil_template, name='perfil'),
    path('<str:slug>/follow', follow, name='follow'),
    path('<str:slug>/unfollow', unfollow, name='unfollow'),
]