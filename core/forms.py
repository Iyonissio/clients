from django import forms
from .models import Client

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'nome',
            'ultimo_nome',
            'idade',
            'salario',
            'email',
            'foto'
        ]
