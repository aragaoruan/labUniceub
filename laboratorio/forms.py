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

        # nome das colunas que sera criado o formulario
        fields = ['nome_laboratorio', 'sigla_laboratorio']
        widgets = {
            # estilizando o form
            'nome_laboratorio':forms.TextInput(attrs={'class':'form-control'}),
            'sigla_laboratorio':forms.TextInput(attrs={'class':'form-control'})
        }