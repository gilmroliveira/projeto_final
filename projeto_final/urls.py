from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core import views

router = routers.DefaultRouter()
router.register(r'categorias', views.CategoriaViewSet)
router.register(r'produtos', views.ProdutoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)), # Centralizador da API
    
    # Rotas das páginas HTML
    path('', views.index, name='index'),
    path('problema/', views.problema, name='problema'),
    path('solucao/', views.solucao, name='solucao'),
    path('autor/', views.autor, name='autor'),
]
# aqui foi criado as rotas para a API usando o DefaultRouter do DRF,
#  e também as rotas para as páginas HTML do Professor usando a função path do Django.