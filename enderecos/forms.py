from django import forms
from .models import Enderecos

class EnderecosForm(forms.ModelForm):
    class Meta:
        model = Enderecos
        fields = [
            'cep',
            'logradouro',
            'numero',
            'bairro',
            'cidade',
            'estado'
        ]

        # Validação de CEP
        def clean_cep(self):
            cep = self.cleaned_data.get('cep')
            cep_limpo = cep.replace('-', '').strip()

            if len(cep_limpo) != 8 or not cep_limpo.isdigit():
                raise forms.ValidationError("Erro: CEP inválido.")

            return cep