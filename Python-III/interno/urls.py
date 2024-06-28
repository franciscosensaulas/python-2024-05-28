from django.urls import path
from . import views


urlpatterns = [
    path("", views.home, name="interno_home"),
    path("categoria", views.categoria_index, name="categorias"),
    path("categoria/cadastrar", views.categoria_cadastrar),
    path("categoria/apagar/<int:id>", views.categoria_apagar),
    path("categoria/editar/<int:id>", views.categoria_editar),

    path("categoria-form", views.categoria_form_index, name="categorias_form"),
    path("categoria-form/cadastrar", views.categoria_form_cadastrar),
    path("categoria-form/apagar/<int:id>", views.categoria_form_apagar),
    path("categoria-form/editar/<int:id>", views.categoria_form_editar),

    
    path("produto", views.produto_index, name="produtos"),
    path("produto/cadastrar", views.produto_cadastrar),
    path("produto/apagar/<int:id>", views.produto_apagar),
    path("produto/editar/<int:id>", views.produto_editar),

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