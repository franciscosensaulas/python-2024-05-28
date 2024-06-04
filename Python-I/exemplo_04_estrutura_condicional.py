def exemplo01():
    numero = int(input("Digite um número: "))
    # Comparar se o número informado é o 10
    if numero == 10: # se
        print("é o número 10")
    else: # senão
        print("é diferente do número 10")
    
    # Operadores relacionais
    # =         Igual
    # >         Maior
    # >=        Maior ou Igual
    # <         Menor
    # <=        Menor ou Igual
    # !=        Diferente 


def exemplo02():
    ano_nascimento = int(input("Digite o seu ano de nascimento: "))
    if ano_nascimento > 2010: # se 
        print("Geração alpha")
    elif ano_nascimento > 1998: # senão se
        print("Geração z")
    elif ano_nascimento > 1981: # senão se
        print("Geração y (millenials)")
    elif ano_nascimento > 1961: # senão se
        print("Geração x")
    else: # senão
        print("Baby boomers")


def exemplo03():
    # nome, quantidade, preço unitário de dois produtos
    # calcular e aplicar desconto
    # solicitar pagamento a vista ou a prazo
    # se for pagamento a vista dar desconto de 5%, caso contrário questionar a quantidade de parcelas
    # se a quantidade de parcelas for maior que 10, acrescentar 18% no valor total
    produto1 = input("Digite o nome do produto: ")
    quantidade1 = int(input("Digite a quantidade: "))
    preco_unitario1 = float(input("Digite o preço unitário: "))

    produto2 = input("Digite o nome do produto: ")
    quantidade2 = int(input("Digite a quantidade: "))
    preco_unitario2 = float(input("Digite o preço unitário: "))

    produto1_total_parcial = quantidade1 * preco_unitario1
    produto2_total_parcial = quantidade2 * preco_unitario2
    total_compra = produto1_total_parcial + produto2_total_parcial

    forma_pagamento = int(input("\n\nFormas de pagamento:\n1 - A vista\n2 - A prazo\nEscolha: "))
    if forma_pagamento == 1:
        valor_desconto = total_compra * 0.05 # calcular 5% de desconto
        valor_a_ser_pago = total_compra - valor_desconto
        print("O valor total da compra é: R$", total_compra)
        print("O valor do desconto é: R$", valor_desconto)
        print("O valor total a ser pago é: R$", valor_a_ser_pago)
    elif forma_pagamento == 2: # verificando que a forma de pagamento é a prazo
        quantidade_parcelas = int(input("Informe a quantidade de parcelas: "))
        if quantidade_parcelas <= 10:
            print("O valor total a ser pago é: R$", total_compra)
        else:
            valor_acrescimo = total_compra * 0.18 # calculando 18% do total da compra
            valor_a_ser_pago = total_compra + valor_acrescimo
            valor_cada_parcela = valor_a_ser_pago / quantidade_parcelas
            print("O valor total da compra é: R$", total_compra)
            print("O valor do juros é: R$", valor_acrescimo)
            print("O valor total a ser pago é: R$", valor_a_ser_pago)
            print("O valor de cada parcela é: R$ ", valor_cada_parcela)
            # Cenário a prazo com juros				Cenário a prazo sem juros		
            # Quantidade Parcelas		11		    Quantidade parcelas		10
            # Juros		32.544		                Juros		0
            # Total a ser pago		213.344		    Total a ser pago		180.8
            # Valor de cada parcela	19.39490909	    Valor de cada parcela		18.08

def exemplo04():
    login = input("Digite o login: ").strip()
    senha = input("Digite a senha: ")
    # Verificando que o login é admin e a senha é 1234
    if login.lower() == "admin" and senha == "1234":
        print("Autenticado, sem bem vindo!")
    else:
        print("Login e/ou senha inválida")
    # Tabela verdade
    # V e V => V
    # F e V => F
    # V e F => F
    # F e F => F


def exemplo05():
    nome = input("Digite o nome do produto").strip()
    produto_vencido_texto = input("Produto vencido? [sim/não] ").strip().lower()
    # Fazendo a sanitização da string (substituindo ',' por '.' e 'R$' por nada)
    preco_unitario = float(input("Digite o preço unitário: R$ ").replace(",", ".").replace("R$", ""))

    # verificar se o usuário digitou 'sim', 's', 'y', 'yes'. Caso positivo o produto é considerado positivo
    if produto_vencido_texto == "sim" or produto_vencido_texto == "s" or produto_vencido_texto == "y" or produto_vencido_texto == "yes":
        produto_vencido = True
    else:
        produto_vencido = False
    # Tabela Verdade
    # V ou V => V
    # F ou V => V
    # V ou F => V
    # F ou F => F


def exemplo_06_par():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("PAR")

def exemplo_07_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 != 0:
        print("ÍMPAR")

# Verificar se número está entre 8k e 9k
# if numero >= 8000 and numero <= 9000

# Ex. 01: Solicite o nome, peso, altura, calcule o imc e a apresentar a classificação (buscar tabela no google)
# Ex. 02: Solicite os 3 lados e apresentar se é um triangulo equilatero, isósceles, escaleno
# Ex. 03: Solicite 3 notas, apresente a média e o status(reprovado, em exame, aprovado)
# Ex. 04: Solicite um caracter e apresente se é vogal ou consoante
# Ex. 05: Solicite um número e apresente se é positivo, negativo ou neutro.
# Ex. 06: Solicite um número e apresente se é ímpar ou negativo
# Ex. 07: Solicite um número e apresente se é maior que 8000
# Ex. 08: Solciite a idade e apresente se é bebê, criança, adolescente, adulto ou idoso
# Ex. 09: Solicite 3 números e apresente qual o menor e qual o maior
# Ex. 10: Solicite 3 números e apresente em ordem crescente
# Ex. 11: Solicite 3 números e apresente em ordem decrescente
# Ex. 12: Solicite os seguintes dados e realize a conversão da temperatura:
#           - Temperatura
#           - Temperatura origem
#           - Temperatura destino
#        Temperaturas suportadas: Celsius, Fahrenheit e Kelvin

    



exemplo05()
