from django.urls import path
<<<<<<< HEAD
from rede_social.views import ContatoSucessoView, ContatoView, index, perfil_template, PostagemView, seguir, desseguir, PostDetalhado
=======
from rede_social.views import ContatoSucessoView, ContatoView, index, perfil_template, PostagemView
>>>>>>> 076ec4b251c448a12cd3d9503697beb30cdeff1f

urlpatterns = [
    path('', index, name="index"),
    path('contato/', ContatoView.as_view(), name='form_contato'),
    path('contato_sucesso/', ContatoSucessoView.as_view(), name='contato_sucesso'),
    path('postagem/', PostagemView.as_view(), name='postagem'),
<<<<<<< HEAD
    path('postagem/<int:pk>', PostDetalhado.as_view(), name='postagem-detalhe'),
    path('<str:slug>', perfil_template, name='perfil'),
    path('<str:slug>/follow', seguir, name='follow'),
    path('<str:slug>/unfollow', desseguir, name='unfollow'),
]
=======
    #path('postagem/'),
    path('<str:slug>/', perfil_template, name='perfil'),
]
>>>>>>> 076ec4b251c448a12cd3d9503697beb30cdeff1f
