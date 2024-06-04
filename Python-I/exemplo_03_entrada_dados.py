import datetime


def exemplo01():
    # input permite o usuário digitar algo que será armazenado dentro de uma variável
    email = input("Digite o seu e-mail: ")
    senha = input("Digite a sua senha: ")
    
    print("E-mail digitado: ", email)
    print("Senha digitada: ", senha)


def exemplo02():
    print("--------------Exemplo 02--------------")
    # Toda entrada utilizando o input vem como str(string texto)
    # Fazemos a conversão de str para int do que o usuário digitou
    idade = int(input("Digite a sua idade: "))
    # Obter o ano atual utilizando o momento atual, obtido através da classe datetime
    ano_atual = datetime.datetime.now().year
    # Calcular o ano de nascimento
    ano_nascimento = ano_atual - idade
    print("Ano de nascimento: ", ano_nascimento)


def exemplo03():
    nome = input("Digite o nome: ")
    sobrenome = input("Digite o sobrenome: ")
    nome_completo = nome + " " + sobrenome
    print("Nome completo: ", nome_completo)


def exemplo04():
   produto = input("Digite o nome do produto: ")
   quantidade = int(input("Digite a quantidade: "))
   preco_unitario = float(input("Digite o preço unitário: "))
   preco = quantidade * preco_unitario
   print("Preço total: ", preco)


# Exercício 01: Criar um algoritmo que solicite o nome, peso e altura
#               Calcular o imc e apresentar o imc
# Exercício 02: Criar um algoritmo que solicite nome, idade, nota 1, nota 2, nota 3
#               Calcular a média (soma das notas/ por quantidade de notas)
#               Apresentar a média
# Exercício 03: Criar um algoritmo que solicite os lados de um retangulo
#               Calcular a área e apresentar 

exemplo04()