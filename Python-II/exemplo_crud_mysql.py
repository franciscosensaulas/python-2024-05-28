import mysql.connector

def conectar():
    # Criando a conexão com o servidor do mysql
    conexao = mysql.connector.connect(
        host="127.0.0.1", # localhost ou 127.0.0.1 é a tua máquina
        port=3306,
        user="root",
        password="admin",
    )
    return conexao


def criar_banco_dados():
    print("Criando banco de dados loja_db")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor.execute("DROP DATABASE IF EXISTS loja_db")
    cursor.execute("CREATE DATABASE loja_db")
    conexao.commit()
    conexao.close()
    # SHOW SCHEMAS;
    print("Banco de dados criado com sucesso")


def definir_banco_dados(cursor):
    # print("Definindo banco dados loja_db")
    cursor.execute("USE loja_db")
    # print("Definido banco dados")
    return cursor

    
def criar_tabela_categorias():
    print("Criando tabela categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("""
                    CREATE TABLE categorias (
                        id INT PRIMARY KEY AUTO_INCREMENT, 
                        nome VARCHAR(100) NOT  NULL
                    )
                   """)
    conexao.commit()
    conexao.close()
    print("Criado tabela categorias")


def inserir_registro_tabela_categorias():
    print("Criando registro na tabela de categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("INSERT INTO categorias (nome) VALUES ('Hatch');")
    conexao.commit()
    conexao.close()
    # SELECT id, nome FROM categorias;
    print("Registro criado com sucesso")
    

def consultar_registros_tabela_categorias():
    print("Consultando registros da tabela de categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # definir o banco de dados que será utilizado, ou seja, USE loja_db
    cursor.execute("SELECT id, nome FROM categorias")
    # Executar a consulta do SELECT buscando todas as categorias
    registros = cursor.fetchall()
    # Percorrendo cada um dos registros para apresentar para o usuário
    for registro in registros:
        print(registro)


criar_banco_dados()
criar_tabela_categorias()
inserir_registro_tabela_categorias()    
consultar_registros_tabela_categorias()
# Ex. Criar um def para criar a tabela de marcas
#       Marcas deve conter os seguintes campos:
#           - id
#           - nome VARCHAR(50)
#           - endereço VARCHAR(150)
# Ex. Criar um def para criar a tabela de clientes
#       Clientes deve conter os seguintes campos:
#           - id
#           - nome VARCHAR(100)
#           - cpf VARCHAR(14)
