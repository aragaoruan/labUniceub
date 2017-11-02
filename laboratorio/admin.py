# importa admin do DJANGO
from django.contrib import admin
#importa Laboratorio de models.py
from laboratorio.models import Laboratorio

"""
adciona no adminstrador do sistema a model Laboratorio
para poder ( criar , deletar, editar) qualquer dados desta model
"""
admin.site.register(Laboratorio)
