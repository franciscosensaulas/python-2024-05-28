import os
# https://dontpad.com/franciscosensaulas
def exemplo_menu():
    limpar_tela()
    apresentar_menu()
    menu_escolhido = int(input("Digite o menu escolhido: "))
    limpar_tela()

    # enquanto o menu escolhido for diferente de sair(20), repetir
    while menu_escolhido != 20:
        # se o menu escolhido for 1, então executará o exemplo de números
        if menu_escolhido == 1:
            exemplo_numeros()
        # senão se o menu escolhido for 2, então executará o exemplo de supermercado
        elif menu_escolhido == 2:
            exemplo_supermercado()
        elif menu_escolhido == 3:
            descobrir_maior_valor()
        elif menu_escolhido == 4:
            descobrir_menor_quantidade_kg_mel()

        apresentar_menu()
        menu_escolhido = int(input("Digite o menu escolhido: "))
        limpar_tela()


def limpar_tela():
    os.system("cls")


def apresentar_menu():
    print("|----------------------------------------------------------------|")
    print("|                         SISTEMA PROWAY                         |")
    print("|----------------------------------------------------------------|")
    print("|  1 - Exemplo números                                           |")
    print("|  2 - Exemplo supermercado                                      |")
    print("|  3 - Exemplo descobrir maior valor                             |")
    print("|  4 - Exemplo descobrir menor valor                             |")
    print("| 20 - Sair                                                      |")
    print("|----------------------------------------------------------------|")

def exemplo_numeros():
    indice, soma_numeros = 0, 0
    while indice < 5:
        numero = int(input("Digite um número: "))
        soma_numeros = soma_numeros + numero
        # incrementar a variável indice em 1
        indice = indice + 1
    media = soma_numeros / 5
    print("Soma: ", soma_numeros)
    print("Média: ", media)


def exemplo_supermercado():
    deseja_cadastrar = ""
    total = 0
    while deseja_cadastrar != "não":
        nome_produto = input("Digite o nome do produto: ").strip() # min: 2 max: 40
        # enquanto o nome do produto conter menos do 2 caracter ou mais do 40, irá 
        # solicitar o nome novamente
        while len(nome_produto) < 2 or len(nome_produto) > 40:
            print("Nome do produto inválido! Mínimo 2 caracteres e máximo 40")
            nome_produto = input("Digite o nome do produto: ").strip() # min: 2 max: 40
        
        quantidade = int(input("Digite a quantidade: "))
        while quantidade <= 0:
            print("Quantidade inválida! Mínimo de uma unidade")
            quantidade = int(input("Digite a quantidade: "))

        preco_unitario = float(input("Digite o preço unitário: ").replace(",", "."))
        while preco_unitario <= 0:
            print("Preço unitário inválido! Preço mínimo de R$ 0,01")
            preco_unitario = float(input("Digite o preço unitário: ").replace(",", "."))

        total_parcial = quantidade * preco_unitario
        total = total + total_parcial
        print("Total parcial: ", total_parcial, end="\n\n")

        deseja_cadastrar = input("Deseja cadastrar outro? [sim/não] ").strip()
    print("Total: ", total)

def descobrir_maior_valor():
    indice = 0
    maior_salario = 0
    while indice < 10:
        salario = float(input("Digite o salário: "))
        if salario > maior_salario:
            maior_salario = salario
        indice = indice + 1
    print("Maior salário: ", maior_salario)
    
def descobrir_menor_quantidade_kg_mel():
    indice = 0
    menor_quantidade_mel = 2_147_483_647
    while indice < 3:
        quantidade_mel = int(input("Digite a quantidade de mel vendida: "))
        if quantidade_mel < menor_quantidade_mel:
            menor_quantidade_mel = quantidade_mel
        indice = indice + 1
    
    print("Menor quantidade de mel: ", menor_quantidade_mel)

        
exemplo_menu()
# Exercícios
# 1. Solicite o nome, preço de 13 peças.
# 2. Solicite a idade para o usuário enquanto que a idade for menor que 128.
# 3. Solicite nomes ao usuário até que o mesmo digite fim para o nome.
# 4. Solicite o peso para o usuário até que o peso seja menor que 0 ou maior que 300,00. 
#    Apresentar ao final a quantidade de pessoas que informaram o peso.
