from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import render
from django.db.models import Prefetch
from django.urls import reverse
from django.views.generic import FormView, TemplateView
from rede_social.forms import ContatoForm
from .models import MensagemDeContato, Pessoa, Postagem

def index(request):
    return HttpResponse('Página Inicial')

def perfil_template(request,slug):
    try:
        perfil = Pessoa.objects.prefetch_related(
        Prefetch('postagem_set', queryset=Postagem.objects.order_by('-data'))
        ).get(slug=slug)

    except Pessoa.DoesNotExist:
        raise Http404('Perfil não encontrado')
        
    return render(request, 'rede_social/perfil.html', {'perfil': perfil})

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