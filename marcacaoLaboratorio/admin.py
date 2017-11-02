# importa admin do DJANGO
from django.contrib import admin
#importa Marcacao de models.py
from marcacaoLaboratorio.models import Marcacao

"""
adciona no adminstrador do sistema a model Laboratorio
para poder ( criar , deletar, editar) qualquer dados desta model
"""
admin.site.register(Marcacao)
