import os
import questionary

from database_operacoes import apagar_registro_tabela_categorias, consultar_registros_tabela_categorias, inserir_registro_tabela_categorias

os.system("cls")



def cadastrar():
    nome = questionary.text("Digite o nome da categoria: ").ask().strip()
    inserir_registro_tabela_categorias(nome)

def editar():
    pass 

def apagar():
    # Consultar as categorias do banco de dados
    categorias = consultar_registros_tabela_categorias()
    # Criar uma lista de Choice para o usuário poder escolher utilizando o questionary
    categorias_choices = []
    for categoria in categorias:
        categorias_choices.append(questionary.Choice(categoria.get("nome"), categoria.get("id")))
    # Perguntar para o usuário qual a categoria que ele deseja apagar
    id_escolhido = questionary.select("Escolha a categoria para apagar:", categorias_choices).ask()
    # Executar o delete na tabela de categorias com o id da categoria escolhida
    apagar_registro_tabela_categorias(id_escolhido)
    print("Registro apagado com sucesso")


def listar_todos():
    from rich.table import Table
    from rich.console import Console
    categorias = consultar_registros_tabela_categorias()
    tabela = Table()
    tabela.add_column("Código")
    tabela.add_column("Nome")
    
    for categoria in categorias:
        tabela.add_row(str(categoria.get("id")), categoria.get("nome"))
    
    console = Console()
    console.print(tabela)


def menu():
    opcao = 0
    while opcao != 1000:
        opcoes = [
            questionary.Choice("Categoria - Listar todos", 1),
            questionary.Choice("Categoria - Cadastro", 2),
            questionary.Choice("Categoria - Editar", 3),
            questionary.Choice("Categoria - Apagar", 4),
            questionary.Choice("Sair", 1000),
        ]
        opcao = int(questionary.select("Escolha o menu:", opcoes).ask())
        
        if opcao == 1:
            listar_todos()
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            editar()
        elif opcao == 4:
            apagar()
        else:
            pass
            
        
menu()