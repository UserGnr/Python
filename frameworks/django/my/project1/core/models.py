from django.db import models

# Create your models here.
class Base(models.Model):
    criado = models.DateField('Data de criação', auto_now_add=True)
    modificado = models.DateField('Data de atualização', auto_now=True)
    ativo = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True

class Produto(Base):
    nome = models.CharField('Nome', max_length=255)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=9)
    imagem = models.ImageField(upload_to='produtos/', default= 'produtos/imagem_padrao.png')

    def __str__(self):
        return self.nome
