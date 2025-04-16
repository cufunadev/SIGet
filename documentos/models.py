from django.db import models

# Create your models here.

from compras.models import SolicitacaoCompra

class Documento(models.Model):
    solicitacao = models.ForeignKey(SolicitacaoCompra, on_delete=models.CASCADE)
    nome_arquivo = models.CharField(max_length=255)
    tipo = models.CharField(max_length=50, blank=True, null=True)
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome_arquivo
