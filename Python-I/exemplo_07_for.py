import time
import questionary


def exemplo01():
    # para indice de 0 até 10 faca
    # começar no 0 e parar no 11
    for indice in range(0, 11):
        print(indice)

    # indice = 0
    # while indice <= 10:
    #     print(indice)
    #     indice = indice + 1


def exemplo_solicitar_numeros():
    # para indice de 0 até 4 faca
    # começar no 0 e parar no 5
    soma_numeros = 0
    for indice in range(5):
        numero = int(input("Digite o número [" + str(indice + 1) + "/5]: "))
        # aculmar a variável número na soma 
        soma_numeros = soma_numeros + numero
    print("Soma dos números: ", soma_numeros)


def exemplo_pokedex():
    # Abrir o arquivo de csv no modo de adição e leitura, e coloca o cursor no final do arquivo
    arquivo = open("pokedex.csv", mode="a+")
    # Mudar o cursor para o começo do arquivo, para que seja possível ler o conteúdo dele
    arquivo.seek(0)
    # Ler todas as linhas do arquivo
    linhas_arquivo = arquivo.readlines()

    print("Pokemons cadastrados: ")
    # Percorrer cada um dos pokemons cadastrados(linhas)
    for indice in range(len(linhas_arquivo)):
        linha = linhas_arquivo[indice]
        linha = linha.replace(";", " => ")
        print(linha, end="")
    
    quantidade_pokemons_desejada = int(questionary.text("Digite a quantidade de pokemons desejada para cadastrar: ").ask())
    for indice in range(quantidade_pokemons_desejada):
        pokemon_nome = questionary.text("Digite o nome do pokemon").ask()
        pokemon_tipo = questionary.select("Escolha o tipo do pokemon: ", ["Água", "Fogo", "Terra", "Planta"]).ask()
        pokemon_codigo = int(questionary.text("Digite o código do pokemon").ask())
        linha = pokemon_nome + ";" + pokemon_tipo + ";" + str(pokemon_codigo) + "\n"
        arquivo.write(linha)

    arquivo.close()


def exemplo_contagem_regressiva():
    # range(inicio, valor para parar, quantidade de incremento/decremento)
    for indice in range(10, -1, -1):
        print(indice)
        # delay de 1 segundo, necessário importar time (import time)
        time.sleep(1)

# Ex. 1: Solicitar o nome, idade de 4 pessoas utilizando comando for
# Ex. 2: Solicitar nome do curso, carga horária, valor do curso e apresentar o valor por hora do curso. 
#        Questionar os dados de 2 cursos
# Ex. 3: Apresentar os números pares até 1000

import os
os.system("cls")
exemplo_contagem_regressiva()