#-*- coding:utf-8 -*-
from django.forms import ModelForm
from django import forms
from marcacaoLaboratorio.models import Marcacao, User
from datetime import datetime

class MarcacaoForm(ModelForm):

    class Meta:
        model = Marcacao
        fields = ['cod_laboratorio', 'hora', 'data', 'data_marcacao', 'cod_user']
        cod_laboratorio = forms.Select(choices=fields)
        widgets = {
            'cod_laboratorio': forms.Select(attrs={'class':'form-control'}),
            'hora':forms.TimeInput(attrs={'class':'form-control', 'type':'time'}),
            'data':forms.DateInput(attrs={'class':'form-control', 'type': 'date'}),
            'data_marcacao':forms.TextInput(attrs={'class':'form-control', 'type': 'hidden', 'value': datetime.now()}),


        }


