from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.base import RedirectView
from rest_framework import viewsets
from .models import *
from .serializer import *
from .forms import *

from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from appsite.models import *
from django.http import HttpResponseRedirect
from django.contrib import messages

# Create your views here.

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventoSerializer
    
def criarEvento(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')    
    else:
        usuario = Estabelecimentos.objects.filter(email = request.user.email)
        for x in usuario:
            tipoUsuario = x.tipoUsuario
            foto = x.foto
            nome = x.nome
        
        form = CriarEventoModel(request.POST or None, request.FILES or None)
        
        if str(request.method) == 'POST':
            if form.is_valid():
                qtdPessoas  = form.cleaned_data['qtdPessoas']
                horaInicial = form.cleaned_data['horaInicial']
                horaFinal   = form.cleaned_data['horaFinal']
                local       = form.cleaned_data['local']
                dataEvento  = form.cleaned_data['dataEvento']
                foto     = form.cleaned_data['foto']
                descricao = form.cleaned_data['descricao']
                titulo = form.cleaned_data['titulo']
                
                id_user = get_object_or_404(Estabelecimentos,email = request.user.email)
                new = Eventos(qtdPessoas = qtdPessoas, horaInicial = horaInicial, horaFinal = horaFinal,local = local,dataEvento = dataEvento,id_estabelecimento=id_user, foto = foto,descricao = descricao, titulo = titulo)

                # messages.success(request, 'Evento cadastrado com sucesso!')
                new.save()
                form = CriarEventoForm()
                return redirect('/dashboard/eventosDisponiveis')

                # print(f'QTD PESSOA: {qtdpessoas}')
                # print(f'Image: {imagem}')

            else:
                messages.error(request, 'Erro ao cadastrar evento!')
    context ={
        'form': form,
        'tipoUsuario' : tipoUsuario,
        'foto' : foto,
        'nomeEsta': nome,
    }
    return render(request, 'criarEvento.html', context)

class EditarEventoView(UpdateView,ListView):
    model = Eventos
    fields = ['titulo','descricao','qtdPessoas', 'horaInicial', 'horaFinal', 'dataEvento', 'local','foto']
    success_url = '/dashboard/eventosDisponiveis'

    def get_context_data(self, **kwargs):
        usuario = Estabelecimentos.objects.filter(email=self.request.user.email)
        
        for x in usuario:
            iduser = x.id
            foto = x.foto
            tipoUsuario = x.tipoUsuario
            nome = x.nome
            
        context = super().get_context_data(**kwargs)
        context['nome'] = nome
        context['iduser'] = iduser
        context['foto'] = foto
        context['tipoUsuario'] = tipoUsuario
        return context

def deleteEventos(request, id):
    eventodelete = get_object_or_404(Eventos, pk=id)
    eventodelete.delete()
    return redirect('/dashboard/eventosDisponiveis')


def Publico_eventos(request,idevento, idpublico):
    try:
        idpublico1 = get_object_or_404(PublicoGeral, pk = idpublico)
        idevento1 = get_object_or_404(Eventos, pk = idevento)
        if Publico_Eventos.objects.filter(idPessoa = idpublico1, idEvento = idevento1):
            # para usar o messages: from django.contrib import messages
            messages.error(request, 'Você já fez uma reserva para esse evento')
            return redirect('/dashboard/suasReservas')
        else: 
            new = Publico_Eventos(idPessoa = idpublico1, idEvento = idevento1)
            new.save()
            messages.success(request, 'Participação concluída, fique atento ao dia e horário do seu evento.')
            return redirect('/dashboard/suasReservas')
    except Exception as e:
        print(e)
        
def deletePublicoEventos(request, idevento, idpublico):
    idpublico1 = get_object_or_404(PublicoGeral, pk = idpublico)
    idevento1 = get_object_or_404(Eventos, pk = idevento)
    
    pe = get_object_or_404(Publico_Eventos,idPessoa = idpublico1, idEvento = idevento1)
    pe.delete()
    return redirect('/dashboard/suasReservas')

def informacoesEventos(request,idevento):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    usuario = Estabelecimentos.objects.filter(email=request.user.email)
    print('\n\n\n\n\n')
    for x in usuario:
        iduser = x.id
        foto = x.foto
        tipoUsuario = x.tipoUsuario
        nome = x.nome
        
    listaPessoas = Publico_Eventos.objects.select_related('idPessoa').filter(idEvento = idevento)
    context ={
        'tipoUsuario' : tipoUsuario,
        'foto' : foto,
        'nomeEsta': nome,
        'listaPessoas':listaPessoas,
        'idevento2': idevento,
    }
    return render(request,'informacoesEvento.html', context)