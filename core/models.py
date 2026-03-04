ffrom django.db import models

class Categoria(models.Model):
    nome = models.CharField(max_length=100) # Ex: Cripto, Forex, Ações

    def __str__(self):
        return self.nome

class Produto(models.Model):
    nome = models.CharField(max_length=100) # Ex: Robô Scalper v1
    preco = models.Decimal_Field(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descricao = models.TextField(default="Estratégia de trading automatizada")

    def __str__(self):
        return self.nome
    # aqui foi criado robos e estrategias de automatizadas de trading. 
