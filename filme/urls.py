from django.urls import path
from .views import Paginaperfil, Homepage, Homefilmes, Detalhesfilme, PesquisaFilme
from django.contrib.auth import views as auth_views

app_name = 'filme'
urlpatterns = [
    path('', Homepage.as_view(), name='homepage'),
    path('filmes/', Homefilmes.as_view(), name='homefilmes'),
    path('filmes/<int:pk>/', Detalhesfilme.as_view(), name='detalhesfilme'),
    path('pesquisa/', PesquisaFilme.as_view(), name='pesquisafilme'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('editarperfil/', Paginaperfil.as_view(), name='editarperfil'),
]