from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser, User


# Create your models here.

# LISTA_TIPOSBEBIDAS = (
#     ('ALCOOLICA', 'Alcoólica'),
#     ('NAO ALCOOLICA', 'Não Alcoólica')
# )


class Estoque(models.Model):
    nome = models.CharField(max_length=50)
    tipo_produto = models.CharField(max_length=15)
    qtd = models.IntegerField(default=0)
    preco_vendas = models.FloatField(default=0)
    total_gasto = models.FloatField(default=0)
    datacriacao_estoque = models.DateTimeField(default=timezone.now)
    estoque = models.ForeignKey(User, related_name='estoque', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=10)
    datacriacao_usuario = models.DateTimeField(default=timezone.now)
    cliente = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)

    def __str__(self):
        return self.nome_cliente


class Vendas(models.Model):
    tipo_bebida = models.CharField(max_length=25)
    bebida = models.CharField(max_length=25)
    qtd = models.IntegerField(default=0)
    valor = models.FloatField(default=0)
    total = models.FloatField(default=0)
    status = models.CharField(max_length=25)
    data_venda = models.DateTimeField(default=timezone.now)
    data_pagamento = models.DateTimeField(default=timezone.now)
    usuario_venda = models.ForeignKey(User, related_name='usuario', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, related_name='cliente', on_delete=models.CASCADE)

    def __str__(self):
        return self.bebida
