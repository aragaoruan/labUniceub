from django.db import models
from django.contrib.auth.models import User

class Laboratorio(models.Model):
    nome_laboratorio = models.CharField(max_length = 100)
    sigla_laboratorio = models.CharField(max_length= 3)

    def __str__(self):
        return self.nome_laboratorio

class Marcacao(models.Model):
    cod_laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE)
    cod_user = models.ForeignKey(User, on_delete=models.CASCADE)
    data_marcacao = models.DateTimeField()
    hora = models.TimeField()
    data = models.DateField()


    def __str__(self):
        return self.data_marcacao