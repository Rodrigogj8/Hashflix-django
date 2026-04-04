from multiprocessing import context
from urllib import request

from django.shortcuts import render, redirect
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class Homepage(TemplateView):
    template_name = "homepage.html"

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('filme:homefilmes')
        else:
            return super().get(request, *args, **kwargs)


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = "homefilmes.html"
    model = Filme
    context_object_name = 'filmes'


class Detalhesfilme(LoginRequiredMixin,DetailView):
    template_name = "detalhesfilme.html"
    model = Filme
    context_object_name = 'filme'

    def get(self, request, *args, **kwargs):
        filmes = self.get_object()
        filmes.visualizacoes += 1
        filmes.save()
        usuario = request.user
        usuario.filmes_vistos.add(filmes)
        return super().get(request, *args, **kwargs) # Retorna a resposta padrão do DetailView

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[:5]
        context['filmes_relacionados'] = filmes_relacionados
        return context
    
class PesquisaFilme(LoginRequiredMixin, ListView):
    template_name = "pesquisa.html"
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            return Filme.objects.filter(titulo__icontains=termo_pesquisa)
        else:
            return Filme.objects.none()
        
class Paginaperfil(LoginRequiredMixin, TemplateView):
    template_name = "editarperfil.html"
        

    



