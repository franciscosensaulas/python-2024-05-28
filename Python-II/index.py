import os
import questionary

from database_operacoes import alterar_registro_tabela_categorias, apagar_registro_tabela_categorias, consultar_registros_tabela_categorias, inserir_registro_tabela_categorias, setup

os.system("cls")



def cadastrar():
    nome = questionary.text("Digite o nome da categoria: ").ask().strip()
    inserir_registro_tabela_categorias(nome)

def editar():
    # Consultar as categorias do banco de dados
    categorias = consultar_registros_tabela_categorias()
    # Verificando se não existe categorias cadastradas
    if len(categorias) == 0:
        print("Nenhuma categoria cadastrada, não sendo possível editar neste momento.")
        # Encerra a execução da função editar, ou seja, não irá apresentar a opção para escolher
        return
    # Criar uma lista de Choice para o usuário poder escolher utilizando o questionary
    categorias_choices = []
    for categoria in categorias:
        categorias_choices.append(questionary.Choice(categoria.get("nome"), categoria))
    # Perguntar para o usuário qual a categoria que ele deseja editar
    categoria_escolhida = questionary.select("Escolha a categoria para editar:", categorias_choices).ask()
    categoria_escolhida["nome"] = questionary.text(
        "Digite o nome da categoria: ", 
        categoria_escolhida.get("nome"),
    ).ask().strip()
    # Chamar a função que executará o update na tabela de categoiras, 
    # para efetivar a atualização na base de dados
    alterar_registro_tabela_categorias(categoria_escolhida.get("id"), categoria_escolhida.get("nome"))

def apagar():
    # Consultar as categorias do banco de dados
    categorias = consultar_registros_tabela_categorias()
    # Verificando se não existe categorias cadastradas
    if len(categorias) == 0:
        print("Nenhuma categoria cadastrada, não sendo possível apagar neste momento.")
        # Encerra a execução da função apagar, ou seja, não irá apresentar a opção para escolher
        return
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
    # Veriifcar se a lista de categorias é vazia
    if len(categorias) == 0:
        # Apresentar mensagem de que não existe categoria cadastrada
        print("Nenhuma categoria cadastrada")
        # return encerrar a execução da função listar_todos, ou seja, não apresentará a tabela
        return
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
            questionary.Choice("Marca - Listar todos", 5),
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

# index.py (menu) adicionar as 4 opções de para marcas
# index.py (menu) adicionar elif para os novos códigos
# index.py criar 4 defs 
#   - listar_todas_marcas()
#   - cadastrar_marca()
#   - editar_marca()
#   - apagar_marca()
# database_operacaoes.py (popular_registros_tabela_marcas) criar 4 registros, 
#       utilizar popular_registros_tabela_categorias como base
# database_operacaoes.py (consultar_registros_tabela_marcas) modificar para 
#       retornar uma lista de dicionários, utilizar consultar_registros_tabela_categorias como base
# index.py (listar_todas_marcas) implementar, utilizar como base index.py (listar_todos)

setup()
menu()