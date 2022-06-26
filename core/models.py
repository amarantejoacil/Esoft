from django.db import models

# Create your models here.


class Endereco(models.Model):
    cep = models.CharField('CEP', max_length=10)
    endereco = models.CharField('Endereço', max_length=200)
    numero_endereco = models.IntegerField('Número de endereço:')
    complemento = models.CharField('Complemento', max_length=150, null=True, blank=True)
    bairro = models.CharField('Bairro', max_length=150)
    cidade = models.CharField('Cidade',max_length=150)
    uf = models.CharField('UF',max_length=2)
    descricao = models.CharField(max_length=150,null=True, blank=True)

    def __str__(self):
        return self.endereco
