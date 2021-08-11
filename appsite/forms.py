from functools import cached_property
from django import forms
from django.db.models import fields
from .models import Estabelecimentos, PublicoGeral

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
        
    def __init__(self,*args, **kwars):
        super().__init__(*args, **kwars)
        self.fields['cep'].widget.attrs.update({'class' : 'mask-cep'})
        
class PublicoForm(forms.Form):
    nome = forms.CharField(label = 'Nome')
    telefone = forms.CharField(label = 'Telefone')
    cidade = forms.CharField(label = 'Cidade')

class PublicoModel(forms.ModelForm):
    class Meta:
        model = PublicoGeral
        fields = ['nome', 'telefone', 'cidade']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs.update({'class' : ''})

