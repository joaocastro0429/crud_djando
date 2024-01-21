from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField(max_length=255)
    preco=models.FloatField()
    validade=models.CharField(max_length=255)
    quantidade=models.IntegerField() 

    # metodos magico para string  

    def __str__(self):
        return self.nome