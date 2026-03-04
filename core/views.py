from django.shortcuts import render
from rest_framework import viewsets
from .models import Categoria, Produto
from .serializers import CategoriaSerializer, ProdutoSerializer

# Visões para a API (DRF)
class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

# Visões para as páginas HTML do Professor
def index(request):
    return render(request, 'index.html')

def problema(request):
    return render(request, 'problema.html')

def solucao(request):
    return render(request, 'solucao.html')

def autor(request):
    return render(request, 'autor.html')
# aqui foi criado as views para a API usando o ModelViewSet do DRF,
#  e também as views para as páginas HTML do Professor usando a função render do Django.