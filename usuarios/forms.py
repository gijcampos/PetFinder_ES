from django import forms
from .models import Cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'telefone', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }