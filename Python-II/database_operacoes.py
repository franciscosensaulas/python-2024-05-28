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


def inserir_registro_tabela_categorias(nome):
    print("Criando registro na tabela de categorias")
    conexao = conectar()
    # Criando cursor que permitirá executar comandos no mysql
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor) # definir o banco de dados que será utilizado, ou seja, USE loja_db
    # cursor.execute("INSERT INTO categorias (nome) VALUES ('Hatch');")
    # cursor.execute("INSERT INTO categorias (nome) VALUES ('" + nome + "');")
    cursor.execute("INSERT INTO categorias (nome) VALUES (%s);", (nome,))
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
    conexao.close()
    # criar a lista de categorias vazia
    categorias = []
    # percorrer cada um dos registros do banco de dados
    for registro in registros:
        # gerar o dicionário (chave, valor) com os dados do registro
        categoria = {
            "id": registro[0],
            "nome": registro[1]
        }
        # adicionar o dicionário(dados da categoria) na lista de categorias
        categorias.append(categoria)
    # a lista de categorias (que contém uma lista de dicionários com os dados das categorias)
    return categorias


def criar_tabela_marcas():
    print("Criando tabela marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
                   CREATE TABLE marcas (
                       id INT PRIMARY KEY AUTO_INCREMENT,
                       nome VARCHAR(50) NOT NULL,
                       endereco VARCHAR(150) NOT NULL
                   )
                   """)
    conexao.commit()
    conexao.close()
    print("Criado tabela marcas")
    
def inserir_registro_tabela_marcas(nome: str, endereco: str):
    print("Criando registro na tabela de marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO marcas (nome, endereco) VALUES (%s, %s)", (nome, endereco))
    conexao.commit()
    conexao.close()
    print("Registro criado com sucesso")


def consultar_registros_tabela_marcas():
    print("Consultando registros da tabela de marcas")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("SELECT id, nome, endereco FROM marcas")
    registros = cursor.fetchall()
    conexao.close()
    for registro in registros:
        print(registro)


def criar_tabela_clientes():
    print("Criando tabela clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("""
                   CREATE TABLE clientes(
                       id INT PRIMARY KEY AUTO_INCREMENT,
                       nome VARCHAR(100) NOT NULL,
                       cpf VARCHAR(14) NOT NULL
                   )
                   """)
    conexao.commit()
    conexao.close()
    print("Criado tabela clientes")
    


def inserir_registro_tabela_clientes(nome: str, cpf: str):
    print("Criando registro na tabela de clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("INSERT INTO clientes (nome, cpf) VALUES (%s, %s)", (nome, cpf))
    conexao.commit()
    conexao.close()
    print("Registro criado com sucesso")


def consultar_registros_tabela_clientes():
    print("Consultando registros da tabela de clientes")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("SELECT id, nome, cpf FROM clientes")
    registros = cursor.fetchall()
    conexao.close()
    for registro in registros:
        print(registro)


def apagar_registro_tabela_categorias(id: int):
    print("Apagando registro da tabela de categorias")
    conexao = conectar()
    cursor = conexao.cursor()
    cursor = definir_banco_dados(cursor)
    cursor.execute("DELETE FROM categorias WHERE id = %s", (id,))
    conexao.commit()
    conexao.close()
    print(f"Apagado registro da tabela de categorias com id = {id}")

# CRUD (Create, Read, Update, Delete)