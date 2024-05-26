from django.db import models
from contas.models import ContaBancaria
from django.utils import timezone

class Transacao(models.Model):
    conta = models.ForeignKey(ContaBancaria, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=[('entrada', 'Entrada'), ('saida', 'Saida')])
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField(default=timezone.now)
    descricao = models.TextField(blank=True)
    consolidada = models.BooleanField(default=False)
    programada = models.BooleanField(default=False)
    data_programada = models.DateField(null=True, blank=True)
    recorrencia = models.IntegerField(default=1)
    pago = models.BooleanField(default=False)
    atrasado = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.descricao} - {self.valor} - {self.conta}"

    def save(self, *args, **kwargs):
        if self.programada and self.recorrencia > 1:
            # Salvar a transação original
            super().save(*args, **kwargs)
            
            # Criar transações adicionais com base na recorrência
            for i in range(1, self.recorrencia):
                nova_data_programada = self.data_programada.replace(day=self.data_programada.day + 30 * i)
                nova_transacao = Transacao(
                    descricao=self.descricao,
                    valor=self.valor,
                    conta=self.conta,
                    programada=self.programada,
                    data_programada=nova_data_programada,
                    consolidada=False,
                    recorrencia=1,  # Zerar a recorrência nas transações adicionais para evitar repetições
                )
                nova_transacao.save()
        else:
            super().save(*args, **kwargs)  # Salvar como de costume
