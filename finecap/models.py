from django.db import models


class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.localizacao


class Reserva(models.Model):
    cnpj = models.CharField(max_length=100)
    quitado = models.BooleanField(default=False)

    nome = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)

    stand = models.OneToOneField(Stand, on_delete=models.CASCADE)

    def __str__(self):
        return f"Reserva da empresa {self.empresa}"
