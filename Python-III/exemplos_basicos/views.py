from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render


def index(request) -> HttpResponse:
    response = HttpResponse(content="""
    <h1>Hello World</h1>
    <a href="contato">Contato</a>
    <a href="/exemplos-basicos/jogo">Jogo</a>                        
    """)
    return response


def contato(request) -> HttpResponse:
    # Obteve o arquivo contato.html e armazenou na variável template
    template = loader.get_template(template_name="contato.html")
    # Renderizar o template armazenando na variável html
    html = template.render(context={}, request=request)
    response = HttpResponse(content=html)
    return response


def jogo(request) -> HttpResponse:
    return render(request, "jogo.html")


def calculadora(request) -> HttpResponse:
    numero1 = 3 # aluno escolheu o número 3
    numero2 = 8 # aluno escolheu o número 8
    soma = numero1 + numero2 # gerar a soma
    contexto_dados = {
        "n1": numero1,
        "n2": numero2,
        "soma": soma
    }
    return render(request, "calculadora.html", context=contexto_dados)


# Criar rota sobre com os seguintes dados no html
#   Nome (aluno escolhe o nome)
#   Sobrenome (aluno escolhe)
#   Nome completo (gerar o nome completo)
#   Idade (aluno escolhe)
#   Ano de Nascimento (gerar o ano nascimento)
#   Peso (aluno escolhe)
#   Altura (Aluno escolhe)
#   Imc (gerar o imc)
#   Imagem

# py manage.py runserver
# http://127.0.0.1:8000/exemplos-basicos/home