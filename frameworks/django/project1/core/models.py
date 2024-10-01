from django.db import models

# Create your models here.
class Produto(models.Model):
    nome = models.CharField('Nome', max_length=100)
    preco = models.DecimalField('Preço', max_digits=9,decimal_places=2)
    estoque = models.IntegerField('Quantidade em Estoque')

class Cliente(models.Model):
    nome = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField("Sobrenome", max_length=100)
    email = models.EmailField('E-mail', max_length=254)