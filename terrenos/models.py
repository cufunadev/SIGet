
from django.db import models
# Create your models here.


class Terreno(models.Model):
    LOCALIZACAO_CHOICES = [
        ('centro', 'Centro'),
        ('bairros', 'Bairros'),
        ('periferia', 'Periferia'),
    ]
    
    localizacao = models.CharField(max_length=20, choices=LOCALIZACAO_CHOICES)
    metragem = models.DecimalField(max_digits=10, decimal_places=2)
    preco = models.DecimalField(max_digits=12, decimal_places=2)
    finalidade = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.localizacao} - {self.metragem}m²"
