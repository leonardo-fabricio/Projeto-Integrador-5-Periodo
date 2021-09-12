from django import forms
from .models import *
from django.forms.widgets import ClearableFileInput

class CriarEventoForm(forms.Form):
    # provavelmente inserir nome (ou outros atributos) da empresa que anunciou o evento, sla
    # vou inserir somente esses por enquanto
    qtdPessoas = forms.IntegerField(label = 'Quantidade de pessoas no evento')
    dataEvento = forms.CharField(label='Data Evento')
    local = forms.CharField(label='Local')
    horaInicial = forms.CharField(label = 'Inicio do Evento')
    horaFinal = forms.CharField(label = 'Hora Final do Evento')
    descricao = forms.CharField(label='descricao')
    titulo = forms.CharField(label='titulo')
    foto = forms.ImageField(label='Imagem', widget = ClearableFileInput)
    
    
class CriarEventoModel(forms.ModelForm):
    class Meta:
        model = Eventos 
        fields = ['titulo','descricao','qtdPessoas', 'horaInicial', 'horaFinal', 'dataEvento', 'local','foto']
        widgets = {
            'titulo': forms.TextInput(attrs={'placeholder':'Insira o titulo aqui'}),
            'descricao': forms.TextInput(attrs={'placeholder':'Descreva seu evento'}),
            'qtdPessoas': forms.TextInput(attrs={'placeholder': 'Quantidade de Pessoas'}),
            'horaInicial': forms.TextInput(attrs={'placeholder': '00:00'}),
            'horaFinal': forms.TextInput(attrs={'placeholder': '00:00'}),
            'dataEvento': forms.TextInput(attrs={'placeholder': 'DD/MM/AAAA'}),
            'local': forms.TextInput(attrs={'placeholder': 'Ex: Av. Tab. Hermes de paiva, 195, Alexandria - RN'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)