from django.db import models
from django.utils import timezone
# Create your models here.

LISTA_TIPOSBEBIDAS = (
    ('ALCOOLICA', 'Alcoólica'),
    ('NAO ALCOOLICA', 'Não Alcoólica')
)


class Estoque(models.Model):
    nome = models.CharField(max_length=50)
    tipo_produto = models.CharField(max_length=15, choices=LISTA_TIPOSBEBIDAS)
    qtd = models.IntegerField(default=0)
    preco_vendas = models.FloatField(default=0)
    total_gasto = models.FloatField(default=0)
    data_criaco = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.nome

