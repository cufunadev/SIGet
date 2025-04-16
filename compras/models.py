from django.db import models
from django.contrib.auth.models import User
from terrenos.models import Terreno

class SolicitacaoCompra(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovada', 'Aprovada'),
        ('rejeitada', 'Rejeitada'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    terreno = models.ForeignKey(Terreno, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pendente')
    data_solicitacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Solicitação {self.id} - {self.usuario}"
