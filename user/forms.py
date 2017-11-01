#-*- coding:utf-8 -*-
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    User._meta.get_field('email').blank = False

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'maxlength': '255'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'maxlength': 255}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'maxlength': 255}),
            'username':forms.TextInput(attrs={'class':'form-control', 'maxlength': 255}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'maxlength': 255}),

        }

        error_messages = {
            'first_name': {
                'required': 'Este campo é obrigatório'
            },
            'last_name': {
                'required': 'Este campo é obrigatório'
            },
            'email': {
                'required': 'Digite um e-mail valido'
            },
            'username': {
                'required': 'Este campo é obrigatório'
            },
            'password': {
                'required': 'Este campo é obrigatório'
            }
        }
    def save(self, commit=True):
        User = super(UserModelForm, self).save(commit=False)
        User.set_password(self.cleaned_data['password'])
        if commit:
            User.save()
        return User