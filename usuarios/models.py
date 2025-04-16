from django.db import models

class Usuario(models.Model):
    TIPO_CHOICES = (
        ('admin', 'Administrador'),
        ('cidadao', 'Cidadão'),
    )

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=255)
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.tipo})"
