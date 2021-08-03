from functools import cached_property
from django import forms
from django.db.models import fields
from .models import Estabelecimentos

class EstabelecimentoForm(forms.Form):
    nome = forms.CharField(label='Nome')
    tipo = forms.CharField(label='Tipo')
    rua = forms.CharField(label='Rua')
    cep = forms.CharField(label='Cep')
    cidade = forms.CharField(label='Cidade')
        
        
class EstabelecimentoModel(forms.ModelForm):
    class Meta:
        model = Estabelecimentos
        fields = ['nome','tipo','rua','cep','cidade']