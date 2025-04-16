from django.db import models

# Create your models here.

from usuarios.models import Usuario

class Notificacao(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)
    data_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notificação para {self.usuario.nome} - {self.data_envio.strftime('%d/%m/%Y')}"
