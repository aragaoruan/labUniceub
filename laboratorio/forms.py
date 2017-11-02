#-*- coding:utf-8 -*-

# importa ModelForms do DJANGO
from django.forms import ModelForm
# importa a models laboratorio (model.py)
from laboratorio.models import Laboratorio
# importa o form do DJANGO
from django import forms

class LaboratorioForm(ModelForm):

    class Meta:
        model = Laboratorio # nome da MODEL
        fields = ['nome_laboratorio', 'sigla_laboratorio'] # nome das colunas que sera criado o formulario
        widgets = {
            # estilizando o form
            'nome_laboratorio':forms.TextInput(attrs={'class':'form-control'}),
            'sigla_laboratorio':forms.TextInput(attrs={'class':'form-control'})
        }