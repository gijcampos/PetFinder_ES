from django import forms
from .models import Cadastro

# ===== PONTE ENTRE O BANCO DE DADOS E O FRONT-END DO USUARIO =====

class CadastroForm(forms.ModelForm):
    class Meta:
        model = Cadastro
        fields = ['nome', 'email', 'telefone', 'senha']
        widgets = {
            'senha': forms.PasswordInput(),
        }

# Validação de requisito minimo de senha
    def clean_senha(self):
        senha = self.cleaned_data.get('senha')
        if len(senha) < 8:
            raise forms.ValidationError("A senha deve ter pelo menos 8 caracteres")
        return senha