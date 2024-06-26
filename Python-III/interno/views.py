from pathlib import Path
from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage

from interno.forms import CategoriaForm
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
    nome = request.POST.get("nome").strip().capitalize()
    # instanciando um objeto da classe Categoria
    # preenchendo os atributos (nome)
    categoria = models.Categoria(nome=nome)
    # Executando a rotina de criar o registro na tabela de Categorias (INSERT INTO)
    categoria.save()
    # Redirecionar para a lista de categorias (categoria_index)
    return redirect("categorias")


# /categoria/apagar/<id>
def categoria_apagar(request, id: int):
    # Buscar a categoria que contém o id que veio na rota
    categoria = models.Categoria.objects.get(pk=id)
    # DELETE FROM categoria WHERE id = 2
    # Executar o delete na tabela de categoria filtrando por id
    categoria.delete()
    # Redireciona para a tela de listagem de categorias
    return redirect("categorias")

# /categoria/editar/<id>
def categoria_editar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    if request.method == "GET":
        contexto = { "categoria": categoria}
        return render(request, "categorias/editar.html", context=contexto)

    categoria.nome = request.POST.get("nome").strip().capitalize()
    categoria.save()
    return redirect("categorias")


# http://127.0.0.1:8000/interno/categoria-form
def categoria_form_index(request):
    # Consultar os registros da tabela de categorias (SELECT)
    categorias = models.Categoria.objects.all()
    contexto = {
        "categorias": categorias
    }
    return render(
        request, 
        "categorias_forms/index.html", 
        context=contexto,
    )


# http://127.0.0.1:8000/interno/categoria-form/cadastrar
def categoria_form_cadastrar(request):
    # Verificando se a request é do tipo POST
    if request.method == "POST":
        # construindo o form com os dados que o usuário preencheu
        form = CategoriaForm(request.POST)
        # valida se o dados preenhcidos que estão no form são válidos
        if form.is_valid():
            # Criar a categoria nesse caso
            form.save()
            # Redirecionar para a lista de categorias
            return redirect("categorias_form")
    # Caso da requisição do tipo GET
    else:
        # Criando o form vazio
        form = CategoriaForm()
    # criando o contexto passando o form
    contexto = {"form": form}
    # retornar o html do form
    return render(request, "categorias_forms/cadastrar.html", context=contexto)


def categoria_form_apagar(request, id: int):
    # Buscar a categoria que contém o id que veio na rota
    categoria = models.Categoria.objects.get(pk=id)
    # DELETE FROM categoria WHERE id = 2
    # Executar o delete na tabela de categoria filtrando por id
    categoria.delete()
    # Redireciona para a tela de listagem de categorias
    return redirect("categorias_form")


def categoria_form_editar(request, id: int):
    categoria = models.Categoria.objects.get(pk=id)
    if request.method == "POST":
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            return redirect("categorias_form")
    else:
        form = CategoriaForm(instance=categoria)
    contexto = {
        "form": form,
        "categoria": categoria,
    }
    return render(request, "categorias_forms/editar.html", contexto)


def produto_index(request):
    produtos = models.Produto.objects.all()
    contexto = {"produtos": produtos}
    return render(request, "produtos/index.html", context=contexto)


def produto_cadastrar(request):
    if request.method == "POST":
        nome = request.POST.get("nome")
        preco = request.POST.get("preco")
        id_categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")
        imagem = __upload_imagem(request)
        produto = models.Produto(
            nome=nome,
            preco=preco,
            descricao=descricao,
            categoria_id=id_categoria,
            imagem=imagem,
        )
        produto.save()
        return redirect("produtos")
    categorias = models.Categoria.objects.all()
    contexto = {"categorias": categorias}
    return render(request, "produtos/cadastrar.html", contexto)


def __upload_imagem(request):
    if not request.FILES:
        return None
    imagem = request.FILES.get("imagem", None)
    if not imagem:
        return None 
    salvador = FileSystemStorage()
    caminho_arquivo = Path("produtos_imagens") / imagem.name
    nome_arquivo = salvador.save(caminho_arquivo, imagem)
    return nome_arquivo


def produto_apagar(request, id: int):
    produto = models.Produto.objects.get(pk=id)
    produto.delete()
    return redirect("produtos")


def produto_editar(request, id: int):
    produto = models.Produto.objects.get(pk=id)

    if request.method == "POST":
        nome = request.POST.get("nome").capitalize()
        preco = request.POST.get("preco")
        id_categoria = request.POST.get("categoria")
        descricao = request.POST.get("descricao")
        produto.nome = nome
        produto.preco = preco
        produto.descricao = descricao
        produto.categoria_id = id_categoria
        produto.save()
        return redirect("produtos")

    categorias = models.Categoria.objects.order_by("nome").all()
    contexto = {
        "categorias": categorias,
        "produto": produto,
    }
    return render(request, "produtos/editar.html", contexto)

# git status
# git add .
# git commit -m "Exemplo de form.Models em categorias-form"
# git push origin main

