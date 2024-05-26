from django import forms
from .models import ContaBancaria

class ContaBancariaForm(forms.ModelForm):
    class Meta:
        model = ContaBancaria
        fields = ['banco', 'nome_titular', 'agencia', 'conta', 'saldo']