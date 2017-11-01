#-*- coding:utf-8 -*-
from django.forms import ModelForm
from laboratorio.models import Laboratorio
from django import forms

class LaboratorioForm(ModelForm):

    class Meta:
        model = Laboratorio
        fields = ['nome_laboratorio', 'sigla_laboratorio']
        widgets = {
            'nome_laboratorio':forms.TextInput(attrs={'class':'form-control'}),
            'sigla_laboratorio':forms.TextInput(attrs={'class':'form-control'})
        }