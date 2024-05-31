# NÃO ESQUECER é necessário instalar o questionary
# Comando para instalar 'pip install questionary'
import questionary 
import os
from typing import List

# função retorna uma string
def exemplo_campo_texto() -> str:
    jogo = questionary.text("Qual o nome do jogo?").ask()
    return jogo

# procedimento
def exemplo_campo_senha() -> str:
    senha_conta_bancaria = questionary.password("Digite a senha da conta bancária: ").ask()
    return senha_conta_bancaria


def exemplo_campo_select() -> str:
    tipo_jogo = questionary.select("Escolha o tipo do jogo: ", ["RPG", "FPS", "Corrida"]).ask()
    return tipo_jogo


def exemplo_campo_checkbox() -> List[str]:
    plataforma = questionary.checkbox(
        "Escolha as plataformas que deseja comprar: ", 
        ["PC", "PS5", "Xbox Series S/X", "Nintendo Switch"],
    ).ask()
    return plataforma


def exemplo_campo_confirmacao() -> bool:
    confirmar_compra = questionary.confirm("Deseja confirmar a compra?").ask()
    return confirmar_compra


def exemplos():
    os.system("cls")
    nome_jogo = exemplo_campo_texto()
    senha = exemplo_campo_senha()
    tipo = exemplo_campo_select()
    plataforma = exemplo_campo_checkbox()
    deseja_comprar = exemplo_campo_confirmacao()
    print(nome_jogo)
    print(senha)
    print(tipo)
    print(plataforma)
    print(deseja_comprar)


exemplos()
