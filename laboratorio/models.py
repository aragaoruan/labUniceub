from django.db import models

class Laboratorio(models.Model):
    nome_laboratorio = models.CharField(max_length = 100)
    sigla_laboratorio = models.CharField(max_length= 3)

    def __str__(self):
        return self.nome_laboratorio

