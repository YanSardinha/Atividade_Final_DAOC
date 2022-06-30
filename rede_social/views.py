from django.http import HttpResponse
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import render, redirect
from django.db.models import Prefetch
from django.urls import reverse, reverse_lazy
from django.views.generic import FormView, TemplateView, DetailView, CreateView
from rede_social.forms import ContatoForm, PostagemForm, NovoComentario
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

    segue = False
    if(perfil.pk != request.user.pessoa.pk and request.user.pessoa.amigos.filter(pk=perfil.id).exists()):
        segue = True

<<<<<<< HEAD
    return render(request, 'rede_social/perfil.html', {'perfil': perfil, 'segue': segue})

@login_required(login_url='/conta/login')
def seguir(request, slug):
    try:
        perfil = Pessoa.objects.get(slug=slug)
    except Pessoa.DoesNotExist:
        raise Http404('Perfil não encontrado.')
    
    if request.user.pessoa.amigos.filter(pk=perfil.id).exists():
        raise HttpResponseForbidden('Você já está seguindo esta pessoa.')

    request.user.pessoa.amigos.add(perfil)

    return redirect('perfil', slug=slug)

@login_required(login_url='/conta/login')
def desseguir(request, slug):
    try:
        perfil = Pessoa.objects.get(slug=slug)
    except Pessoa.DoesNotExist:
        raise Http404('Perfil não encontrado')
    
    if not request.user.pessoa.amigos.filter(pk=perfil.id).exists():
        return HttpResponseForbidden('Você não segue essa pessoa')
        
    request.user.pessoa.amigos.remove(perfil)

    return redirect('perfil', slug=slug)

class PostagemView(LoginRequiredMixin, CreateView):
    login_url = '/conta/login/'
=======
class PostagemView(LoginRequiredMixin, CreateView):
>>>>>>> 076ec4b251c448a12cd3d9503697beb30cdeff1f
    template_name = 'rede_social/postagem.html'
    form_class = PostagemForm
    model = Postagem

    def form_valid(self, form):
        postagem = form.save(commit=False)
        postagem.pessoa =self.request.user.pessoa
        postagem.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')

class PostDetalhado(DetailView):
    model = Postagem
    template_name = 'rede_social/post_detalhe.html'
    context_object_name = 'postagem'

    def get_context_data(self, **kwargs):
        context = super(PostDetalhado, self).get_context_data(**kwargs)
        context['form'] = NovoComentario
        return context

    def post(self, request, *args, **kwargs):
        form = NovoComentario(request.POST, request.FILES)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.pessoa = request.user.pessoa
            comentario.postagem = self.get_object()
            comentario.save()

        self.object = self.get_object()
        context = super(PostDetalhado, self).get_context_data(**kwargs)
        context['form'] = NovoComentario
        return self.render_to_response(context=context)