from django.contrib import admin
from django.urls import path, include
from . import views as views_setup # 'as' seria um apelido para aquele import
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exemplos-basicos', include("exemplos_basicos.urls")),
    path('interno', include('interno.urls')),
    path('publico', include('publico.urls')),
    path('', views_setup.home),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)