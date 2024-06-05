import os
import questionary

from database_operacoes import consultar_registros_tabela_categorias, inserir_registro_tabela_categorias

os.system("cls")


def listar_todos():
    consultar_registros_tabela_categorias()

def cadastrar():
    nome = questionary.text("Digite o nome da categoria: ").ask().strip()
    inserir_registro_tabela_categorias(nome)

def editar():
    pass 

def apagar():
    pass

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