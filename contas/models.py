from django.db import models
from django.contrib.auth.models import User

class ContaBancaria(models.Model):
    banco = models.CharField(max_length=100)
    nome_titular = models.CharField(max_length=100)
    agencia = models.CharField(max_length=100)
    conta = models.CharField(max_length=100)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nome_titular} - {self.banco} - {self.agencia} - {self.conta}"
