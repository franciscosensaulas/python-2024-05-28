# Criar novo projeto
```
py manage.py startapp nome_app
```

# Adicionar o app no settings.py
Adicionar no `INSTALLED_APPS` o nome do app criado no arquivo settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    ...
    'nome_app',
]
```

# Criar arquivo urls.py no app que foi criado

# Criar a classe dentro do arquivo de models.py 
Estado:
id 
nome 
sigla

# Criar a migration 
py .\manage.py makemigrations interno
# Atualizar o banco aplicando as migrations
py manage.py migrate

# Adicionar nas rotas urls.py
Adicionar as rotas do CRUD de estados
# Adicionar no views.py as funções(def) pertinentes ao CRUD de estados
estado_index (primeiro)
estado_cadastrar
estado_apagar   
estado_editar
# Criar os templates
Criar pasta estados dentro de templates
Criar os arquivos de html dentreo de templates/estados:
- index.html (primeiro)
- cadastrar.html
- editar.html