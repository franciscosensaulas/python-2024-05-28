from django.urls import path
from . import views

# Informando quais serão as rotas do nosso app exemplos_basicos
urlpatterns = [
    # quando a rota exemplos-basicos/home for acessada irá executar o código da função home do arquivo views.py
    path("/home", views.index),
    path("/", views.index),
    path("/contato", views.contato),
    path("/jogo", views.jogo),
    path("/calculadora", views.calculadora),
]