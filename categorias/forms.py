from django import forms
from .models import Categoria, Subcategoria

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome']
    def __init__(self,  *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CategoriaForm, self).__init__(*args, **kwargs)
        if user:
            self.instance.usuario = user

class SubcategoriaForm(forms.ModelForm):
    class Meta:
        model = Subcategoria
        fields = ['nome']
