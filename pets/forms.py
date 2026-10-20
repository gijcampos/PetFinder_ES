from django import forms
from .models import Pets 

#formularios dos Pets

class PetsForm(forms.ModelForm):
    class Meta:
        model = Pets
        fields = [
            'nome',
            'especie',
            'raca',
            'idade',
            'id_disp_rastreamento',
            'tutor'
        ]