from django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100)
    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return self.nome
    # aqui eu criei duas classes uma para
    #  categoria e outra para produto, onde o produto tem um campo de chave
    #  estrangeira para a categoria, ou seja, cada produto pertence a uma categoria.
