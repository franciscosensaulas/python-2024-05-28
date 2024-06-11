# Exercício de tabelas relacionadas
Criar uma tabela de contatos que permitirá adicionar contatos para os clientes registrados
- database_operacoes.py criar def criar_tabela_contatos (utilizar como exemplo criar_tabela_produtos) para criar a tabela de contatos com os seguintes campos:
  - id PK
  - id_cliente FK 
  - tipo VARCHAR(10) (E-mail, Celular, Telefone, Insta)
  - valor VARCHAR(100)
- database_operacoes.py criar def popular_registros_tabela_contatos, registrando 2 contatos para o primeiro cliente e 1 para outro cliente
- database_operacoes.py criar def consultar_registros_tabela_contatos, que fará o select na tabela de contatos com inner join da tabela de clientes, construir uma lista de dicionários com os clientes da consulta (registros)
- index.py adicionar menu de CRUD do contato
- index.py criar def listar_todos_contatos, apresentar tabela com os registros retornados da função consultar_registros_tabela_contatos