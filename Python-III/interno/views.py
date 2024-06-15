from django.shortcuts import render, redirect
from . import models


def home(request):
    return render(request, "home.html")


def categoria_index(request):
    # Consultar os registros da tabela de categorias (SELECT)
    categorias = models.Categoria.objects.all()
    contexto = {
        "categorias": categorias
    }
    return render(
        request, 
        "categorias/index.html", 
        context=contexto,
    )


def categoria_cadastrar(request):
    if request.method == "GET":
        return render(request, "categorias/cadastrar.html")
    # Obtendo os dados que o usuário preencheu nos campos
    nome = request.POST.get("nome").strip()
    # instanciando um objeto da classe Categoria
    # preenchendo os atributos (nome)
    categoria = models.Categoria(nome=nome)
    # Executando a rotina de criar o registro na tabela de Categorias (INSERT INTO)
    categoria.save()
    # Redirecionar para a lista de categorias (categoria_index)
    return redirect("categorias")


def categoria_apagar(request):
    pass


def categoria_editar(request):
    pass

