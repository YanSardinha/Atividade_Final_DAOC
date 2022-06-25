from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.db.models import Prefetch
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView
from rede_social.forms import ContatoForm, MensagemForm
from .models import MensagemDeContato, Pessoa, Postagem, Comentario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

#<!---------------AUTENTICAÇÃO NÃO NECESSÁRIA----------------------!>#

class ContatoView(FormView):
    template_name = 'rede_social/contato.html'
    form_class = ContatoForm

    def form_valid(self, form):
        dados = form.clean()
        mensagem = MensagemDeContato(nome=dados['nome'], email=dados['email'], mensagem=dados['mensagem'])
        mensagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('contato_sucesso')

class ContatoSucessoView(TemplateView):
    template_name = 'rede_social/contato_sucesso.html'

#<!---------------AUTENTICAÇÃO NECESSÁRIA----------------------!>#
@login_required(login_url='/conta/login')
def index(request):
    postagem = Postagem.objects.order_by("-id")
    return render(request, 'rede_social/index.html',{'postagem': postagem})

@login_required(login_url='/conta/login')
def perfil_template(request,slug):
    try:
        perfil = Pessoa.objects.prefetch_related(
        Prefetch('postagem_set', queryset=Postagem.objects.order_by('-data'))
        ).get(slug=slug)

    except Pessoa.DoesNotExist:
        raise Http404('Perfil não encontrado')

    return render(request, 'rede_social/perfil.html', {'perfil': perfil})

class MensagemView(LoginRequiredMixin,FormView):
    login_url = reverse_lazy('login')
    template_name = 'rede_social/mensagem.html'
    form_class = MensagemForm

    def form_valid(self, form):
        dados = form.clean()
        conteudo = Postagem(pessoa = self.request.user.pessoa, conteudo = dados['publicacao'])
        conteudo.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')
