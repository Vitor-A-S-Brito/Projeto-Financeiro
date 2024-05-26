from django import forms
from .models import Transacao

class TransacaoForm(forms.ModelForm):
    programada = forms.DateField(required=False, widget=forms.DateInput(attrs={'type': 'date'}))
    recorrente = forms.IntegerField(required=False)

    class Meta:
        model = Transacao
        fields = ['conta', 'tipo', 'valor', 'descricao', 'programada', 'recorrente']
