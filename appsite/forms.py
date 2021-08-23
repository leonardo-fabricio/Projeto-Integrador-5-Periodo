from functools import cached_property
from django import forms
from django.db.models import fields
from django.forms.widgets import ClearableFileInput
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
    telefone = forms.CharField(label = 'Telefone')
    cidade = forms.CharField(label = 'Cidade')

class PublicoModel(forms.ModelForm):
    class Meta:
        model = PublicoGeral
        fields = ['telefone', 'cidade']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['telefone'].widget.attrs.update({'class' : ''})

# Criando parte de Criação de Eventos Form
class CriarEventoForm(forms.Form):
    # provavelmente inserir nome (ou outros atributos) da empresa que anunciou o evento, sla
    # vou inserir somente esses por enquanto
    qtdPessoas = forms.IntegerField(label = 'Quantidade de pessoas no evento')
    dataEvento = forms.CharField(label='Data Evento')
    local = forms.CharField(label='Local')
    horaInicial = forms.CharField(label = 'Inicio do Evento')
    horaFinal = forms.CharField(label = 'Hora Final do Evento')
    imagem = forms.ImageField(label='Imagem', widget = ClearableFileInput)
    

class CriarEventoModel(forms.ModelForm):
    class Meta:
        model = Eventos
        fields = ['qtdPessoas', 'horaInicial', 'horaFinal', 'dataEvento', 'local','imagem']
        widgets = {
            'qtdPessoas': forms.TextInput(attrs={'placeholder': 'Quantidade de Pessoas'}),
            'horaInicial': forms.TextInput(attrs={'placeholder': '00:00'}),
            'horaFinal': forms.TextInput(attrs={'placeholder': '00:00'}),
            'dataEvento': forms.TextInput(attrs={'placeholder': 'dd/mm/aaaa'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

