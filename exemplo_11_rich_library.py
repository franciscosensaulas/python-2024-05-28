import os
from rich.console import Console
from rich.table import Table


def exemplo_tabela():
    # instanciando um objeto de Tabela
    tabela = Table(show_header=True)
    # adicionando as colunas na tabela
    tabela.add_column("Modelo")
    tabela.add_column("Ano Fabricação")
    tabela.add_column("Preço")
    
    # Adicionando as linhas preenchendo o valor para cada uma das colunas
    tabela.add_row("Gol Quadrado", "1990", "R$ 14.900,00")
    tabela.add_row("Uno com escada", "1981", "R$ 9.530,00")

    # instanciando um objeto de Console
    console = Console()
    # apresentar a tabela
    console.print(tabela)


exemplo_tabela()


# Ex. 1: Criar um vetor para armazenar 6 e-mails e apresentar eles
# Ex. 2: Criar vetores para armazenar nome, peso, altura. 
#           Preencher os vetores solicitando esses dados para o usuário.
#           Calcular o imc de cada um armazenando em outro vetor.
#           Apresentar nome e imc de cada registro armazenado nos vetores.
#           Solicitar para 3 pessoas.