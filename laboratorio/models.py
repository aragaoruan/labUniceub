# importando o models no DJANGO
from django.db import models

class Laboratorio(models.Model): # nome da tabela que sera criado no banco de dados

    nome_laboratorio = models.CharField(max_length = 100) # nome da coluna, tipo e tamanho maximo
    sigla_laboratorio = models.CharField(max_length= 3) # nome da coluna, tipo e tamanho maximo

    # funcao de retorno quando se faz um SELECT
    def __str__(self):
        return self.nome_laboratorio # por DEFAULT vem o nome_laborario


#   O CREATE GERADO SERA ESSE
    """
    CREATE TABLE laboratorio_laboratorio 
        (
            "id" serial NOT NULL PRIMARY KEY,
            "nome_laboratorio" varchar(100) NOT NULL,
            "sigla_laboratorio" varchar(3) NOT NULL
        );
    
    """


