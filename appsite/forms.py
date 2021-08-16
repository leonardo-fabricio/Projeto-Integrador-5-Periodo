from functools import cached_property
from django import forms
from django.db.models import fields
from .models import Estabelecimentos, PublicoGeral, Eventos

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

# Criando parte de Criação de Eventos Form
class CriarEventoForm(forms.Form):
    # provavelmente inserir nome (ou outros atributos) da empresa que anunciou o evento, sla
    # vou inserir somente esses por enquanto
    qtdPessoas = forms.CharField(label = 'Quantidade de pessoas no evento')
    horaInicial = forms.DateTimeField(label = 'Inicio do Evento')
    horaFinal = forms.DateTimeField(label = 'Hora Final do Evento')

class CriarEventoModel(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['qtdPessoas', 'horaInicial', 'horaFinal']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


