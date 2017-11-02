#-*- coding:utf-8 -*-

# importa ModelForms do DJANGO
from django.forms import ModelForm
# importa o form do DJANGO
from django import forms
# importa a models Marcacao (model.py)
from marcacaoLaboratorio.models import Marcacao
# importa datetime do PYTHON
from datetime import datetime

class MarcacaoForm(ModelForm):

    class Meta:
        model = Marcacao # nome da MODEL

        # nome das colunas que sera criado o formulario
        fields = ['cod_laboratorio', 'hora', 'data', 'data_marcacao', 'cod_user']
        cod_laboratorio = forms.Select(choices=fields)
        widgets = {
            # estilizando o form
            'cod_laboratorio': forms.Select(attrs={'class':'form-control'}),
            'hora':forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'data':forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'data_marcacao':forms.TextInput(attrs={'class':'form-control', 'type': 'hidden', 'value': datetime.now()}),
        }


