# importando o models no DJANGO
from django.db import models
# imporatando model user do DJANGO
from django.contrib.auth.models import User
# importando do APP laboratorio ( laboratorio/models.py)
from laboratorio.models import Laboratorio

class Marcacao(models.Model): # nome da tabela que sera criado no banco de dados

    cod_laboratorio = models.ForeignKey(Laboratorio, on_delete=models.CASCADE) # nome da coluna, tipo e tamanho maximo
    cod_user = models.ForeignKey(User, on_delete=models.CASCADE) # nome da coluna, tipo e tamanho maximo
    data_marcacao = models.DateTimeField() # nome da coluna, tipo e tamanho maximo
    hora = models.TimeField() # nome da coluna, tipo e tamanho maximo
    data = models.DateField() # nome da coluna, tipo e tamanho maximo

    # funcao de retorno quando se faz um SELECT
    def __str__(self):
        return self.data_marcacao # por DEFAULT vem o data_marcacao

    #   O CREATE GERADO SERA ESSE
    """
    CREATE TABLE marcacaoLaboratorio_marcacao
         (
            id integer PRIMARY KEY AUTOINCREMENT,
            cod_laboratorio INT(4) NOT NULL,
            cod_user INT(4) NOT NULL,
            data_marcacao DATETIME,
            hora DATE ,
            data TIME ,
            FOREIGN KEY (cod_laboratorio) references laboratorio_laboratorio(id),
            FOREIGN KEY (cod_user) references auth_user(id),
         );
    """