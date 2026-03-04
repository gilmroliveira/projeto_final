from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import CategoriaViewSet, ProdutoViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'produtos', ProdutoViewSet)

urlpatterns = [
    # path('admin/', admin.site.urls), # se quiser manter o admin
    path('api/', include(router.urls)),
    # coloque aqui o path da sua página 'home' original
]
# aqui eu criei um router para registrar as minhas viewsets de categoria e produto,
#  e depois incluí o router nas minhas urls,
#  para que eu possa acessar a minha API através do endpoint /api/categorias/ e /api/produtos/.   