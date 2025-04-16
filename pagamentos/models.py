from django.db import models

# Create your models here.

from compras.models import SolicitacaoCompra

class Pagamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('pago', 'Pago'),
        ('cancelado', 'Cancelado'),
    ]

    solicitacao = models.ForeignKey(SolicitacaoCompra, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_pagamento = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')

    def __str__(self):
        return f"Pagamento #{self.id} - R${self.valor}"
