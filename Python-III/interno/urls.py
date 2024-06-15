from django.urls import path
from . import views


urlpatterns = [
    path("/categoria", views.categoria_index, name="categorias"),
    path("/categoria/cadastrar", views.categoria_cadastrar),
    path("/categoria/apagar/<int:id>", views.categoria_apagar),
    path("/categoria/editar/<int:id>", views.categoria_editar),
]

# Criar app
# Criar o arquivo urls
# Criar os models
# Gerar as migrations (py manage.py makemigrations nome_app)
# Aplicar as migrations  (py manage.py migrate)
# Adicionar as rotas no arquivo de urls.py do novo app
# Adicionar include do novo arquivo de rotas no urls.py do setup
# Criar pasta templates
# Criar as views no arquivo de views.py
# Criar os arquivos na pasta templates