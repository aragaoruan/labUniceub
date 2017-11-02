# importando AppConfig do DJANGO
from django.apps import AppConfig

# Classe que determina o nome do APP
"""
esse nome deve ser o mesmo que é colocado no arquivo 
settings.py dentro do array INSTALLED_APPS

"""
class MarcacaolaboratorioConfig(AppConfig):
    name = 'marcacaoLaboratorio'
