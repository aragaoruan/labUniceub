#-*- coding:utf-8 -*-

# importa ModelForms do DJANGO
from django import forms
# importa User do DJANGO
from django.contrib.auth.models import User

class UserModelForm(forms.ModelForm):
    # para a coluna e-mail sempre vim em branco
    User._meta.get_field('email').blank = False

    class Meta:
        model = User # nome da MODEL

        # nome das colunas que sera criado o formulario
        fields = ['username', 'first_name', 'last_name', 'email', 'password']
        widgets = {
            # estilizando o form
            'first_name':forms.TextInput(attrs={'class':'form-control', 'maxlength': '255'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'maxlength': 255}),
            'email':forms.EmailInput(attrs={'class':'form-control', 'maxlength': 255}),
            'username':forms.TextInput(attrs={'class':'form-control', 'maxlength': 255}),
            'password':forms.PasswordInput(attrs={'class':'form-control', 'maxlength': 255}),

        }

    # funcao para antes de salvar encriptar a senha
    def save(self, commit=True):
        User = super(UserModelForm, self).save(commit=False)
        User.set_password(self.cleaned_data['password'])
        if commit:
            User.save()
        return User