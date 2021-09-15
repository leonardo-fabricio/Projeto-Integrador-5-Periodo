
import random
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic.edit import UpdateView
from django.views.generic.list import ListView
from .forms import *
from .models import *
from django.contrib import messages
from rest_framework import viewsets
from appsite.serializer import *
from reportlab.lib.pagesizes import A4
from .utils import *
import requests
import json
from random import sample
import re

url1 = 'http://localhost:3000/api-evento/'
url2 = 'http://127.0.0.1:3000/api-publico_eventos/'


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/eventosDisponiveis')
    return render(request,'index.html')

def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'profile.html', {})

def dashboard(request): 
    seus_eventos = ''
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    elif not (PublicoGeral.objects.filter(email = request.user.email) or (Estabelecimentos.objects.filter(email=request.user.email))): 
        return redirect('/escolha')
    else:
        if PublicoGeral.objects.filter(email = request.user.email):
            usuario = PublicoGeral.objects.filter(email = request.user.email)
            print('\n\n\n\n\n')
            for x in usuario:
                iduser = x.id
                foto = x.foto
                tipoUsuario = x.tipoUsuario
                nome = x.nome
                
        else:
            usuario = Estabelecimentos.objects.filter(email=request.user.email)
            print('\n\n\n\n\n')
            for x in usuario:
                iduser = x.id
                foto = x.foto
                tipoUsuario = x.tipoUsuario
                nome = x.nome
                # print(tipoUsuario)
            
            # seus_eventos = Eventos.objects.filter(id_estabelecimento = id_user)
    
    url1 = 'http://localhost:3000/listAll'
    headers={'Content-Type': 'application/json'} 
    response = requests.get(url1, headers= headers)
    
    response = json.loads(response.content)
    
    eventos = response
    
    seus_eventos = []
    
    countEventos = 0
    countEventosPessoa = 0
    
    for x in eventos:
        countEventos += 1
        if x['id_estabelecimento'] == iduser:
            seus_eventos.append(x)
            # print(type(x['_id']))
            # print('\n\n\n\n')
           

    url2 = 'http://127.0.0.1:3000/listallpe/'
    resposta = requests.get(url2)
    resposta = json.loads(resposta.content)
    for x in resposta:
        if x['id_publico'] == iduser:
            countEventosPessoa += 1
          
    content = {
        'tipoUsuario' : tipoUsuario,
        'eventos' : eventos,
        'seus_eventos' : seus_eventos,
        'foto' : foto,
        'iduser': iduser,
        'nomeEsta' : nome,
        'countEventos': countEventos,
        'countEventosPessoa': countEventosPessoa,
    }
    
    return render(request, 'eventosDisponiveis.html', content) 

def cadastroEstabelecimento(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    form = EstabelecimentoModel(request.POST or None, request.FILES or None)
    
    if form.is_valid():
        nome   = form.cleaned_data['nome']
        tipo   = form.cleaned_data['tipo']
        foto   = form.cleaned_data['foto']
    
        if Estabelecimentos.objects.filter(email = request.user.email):
            new_p = Estabelecimentos.objects.get(email = request.user.email)
            new_p.nome = nome
            new_p.foto = foto
            new_p.tipo = tipo
            new_p.save()
        else:
            new = Estabelecimentos(nome = nome,tipo = tipo, email = request.user.email, foto= foto, tipoUsuario = 'estabelecimento')
            new.save()
        
        form = EstabelecimentoForm()
        return redirect('/dashboard/eventosDisponiveis')
  
    context = {
        'form' : form,
    }
    return render(request,'cadastroEstabelecimento.html',context)

def cadastroPublico(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    form = PublicoModel(request.POST or None, request.FILES or None)
    if str(request.method) == 'POST' : 
        if form.is_valid():
            cidade   = form.cleaned_data['cidade']
            telefone = form.cleaned_data['telefone'] # eu sei 
            foto     = form.cleaned_data['foto']
            nome     = form.cleaned_data['nome'] 
            if PublicoGeral.objects.filter(email = request.user.email):
                new_p = PublicoGeral.objects.get(email = request.user.email)
                new_p.telefone = telefone
                new_p.cidade = cidade
                new_p.foto = foto
                new_p.nome = nome
                new_p.save()
            else:
                new = PublicoGeral(nome = nome, cidade = cidade, telefone = telefone, email = request.user.email, foto = foto, tipoUsuario = 'normal')
                new.save()
            
            form = PublicoForm()
            return redirect('/dashboard/eventosDisponiveis')
  
    context = { 
        'form' : form,
    }
    return render(request, 'cadastroPublico.html',context)

def suasReservas(request): 
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    else:
        usuario = PublicoGeral.objects.filter(email = request.user.email)
        for x in usuario:
            tipoUsuario = x.tipoUsuario
            foto = x.foto
            iduser = x.id
            nome = x.nome

    url1 = 'http://localhost:3000/listAll/'
    url2 = 'http://127.0.0.1:3000/listallpe/'
   
    resposta = requests.get(url2)
    resposta = json.loads(resposta.content)
    
    countEventosPessoa = 0
    countEventos = 0
    
    ids = []
    for x in resposta:
        if x['id_publico'] == iduser:
            ids.append(x['id_evento'])
            countEventosPessoa += 1
            
    resposta = requests.get(url1)
    resposta = json.loads(resposta.content)
    eventos = resposta
    peventos = []
    
    for x in eventos:
        countEventos += 1
        for y in ids:
            if x['id_auxiliar'] == y:
                peventos.append(x)
                
    content = {
        'tipoUsuario' : tipoUsuario,
        'foto' : foto,
        'event' : peventos,
        'iduser' : iduser,
        'nomeEsta': nome,
        'countEventos': countEventos,
        'countEventosPessoa': countEventosPessoa,
    }
    return render(request, 'suasReservas.html', content)

def escolha(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')

    return render(request, 'escolha.html')

def informacoesEventos(request,idauxiliar):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    
    usuario = Estabelecimentos.objects.filter(email=request.user.email)
    print('\n\n\n\n\n')
    for x in usuario:
        iduser = x.id
        foto = x.foto
        tipoUsuario = x.tipoUsuario
        nome = x.nome
        
    # url = f'http://127.0.0.1:3000/api-evento/{idevento}/'
    
    url1 = 'http://localhost:3000/listAll/'
    url2 = 'http://127.0.0.1:3000/listallpe/'
    
    response = requests.get(url2) 
    response = json.loads(response.content)
    
    list_aux=[]
    
    for x in response:
        if x['id_evento'] == idauxiliar:
            list_aux.append(x['id_publico'])
    
    listaPessoas = []
    
    for x in list_aux:
        if PublicoGeral.objects.filter(pk = x):
            listaPessoas.append(PublicoGeral.objects.get(pk = x))
        
    # listaPessoas = Publico_Eventos.objects.select_related('idPessoa').filter(idEvento = idevento)
    context ={
        'tipoUsuario' : tipoUsuario,
        'foto' : foto,
        'nomeEsta': nome,
        'listaPessoas':listaPessoas,
        'idevento2': idauxiliar,
    }
    return render(request,'informacoesEvento.html', context)

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
                fotoevento     = form.cleaned_data['foto']
                descricao = form.cleaned_data['descricao']
                titulo = form.cleaned_data['titulo']
                id_evento = random.randint(1,10000)
                
                
                
                url2 = 'http://127.0.0.1:3000/listAll'
                headers={'Content-Type': 'application/json'} 
                response = requests.get(url2, headers= headers)
                response = json.loads(response.content)
                eventos = response
                print(id_evento)
                print('\n\n\n\n')
                
                for x in eventos:
                    while x['id_auxiliar'] == id_evento:
                        id_evento = random.randint(1,10000)
                    
                
                id_user = Estabelecimentos.objects.get(email = request.user.email)
                url = 'http://localhost:3000/api-evento' 
                event_data = {
                    'titulo': f'{titulo}', 
                    'descricao': f'{descricao}', 
                    'qtdPessoas': qtdPessoas, 
                    'dataEvento': f'{dataEvento}', 
                    'horaInicial': f'{horaInicial}', 
                    'horaFinal': f'{horaFinal}', 
                    'local': f'{local}', 
                    'id_estabelecimento': f'{id_user.id}',
                    'id_auxiliar' : f'{id_evento}'
                    # 'foto': f'{fotoevento}', 
                }

                response = requests.post(url = url, json = event_data)
                if response.status_code >=200 and response.status_code <= 299:
                    messages.success(request, 'Evento cadastrado com sucesso!')
            
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
 
def EditarEvento(request, idauxiliar):
    form = CriarEventoModel(request.POST or None, request.FILES or None)
    usuario = Estabelecimentos.objects.filter(email= request.user.email)
    
    for x in usuario:
        iduser = x.id
        foto = x.foto
        tipoUsuario = x.tipoUsuario
        nome = x.nome
        
    
    if form.is_valid():
        qtdPessoas  = form.cleaned_data['qtdPessoas']
        horaInicial = form.cleaned_data['horaInicial']
        horaFinal   = form.cleaned_data['horaFinal']
        local       = form.cleaned_data['local']
        dataEvento  = form.cleaned_data['dataEvento']
        fotoevento     = form.cleaned_data['foto']
        descricao = form.cleaned_data['descricao']
        titulo = form.cleaned_data['titulo']

        event_data = {
            'titulo': f'{titulo}', 
            'descricao': f'{descricao}', 
            'qtdPessoas': qtdPessoas, 
            'dataEvento': f'{dataEvento}', 
            'horaInicial': f'{horaInicial}', 
            'horaFinal': f'{horaFinal}', 
            'local': f'{local}',
            'id_estabelecimento': f'{iduser}',
            'id_auxiliar': f'{idauxiliar}',
        }
        url1 = 'http://localhost:3000/listAll'
        url = ''
        headers={'Content-Type': 'application/json'} 
        response = requests.get(url1, headers= headers)
        response = json.loads(response.content)
        eventos = response
        
        for x in eventos:
            if x['id_auxiliar'] == idauxiliar:
                url = f"http://127.0.0.1:3000/editar/{x['_id']}"
                
        response = requests.put(url = url, json = event_data)
        form = CriarEventoForm()
        return redirect('/dashboard/eventosDisponiveis')
    
    context = {}
    context['nomeEsta'] = nome
    context['iduser'] = iduser
    context['foto'] = foto
    context['tipoUsuario'] = tipoUsuario
    context['form'] = form
    context['idevento'] = idauxiliar
    # context['resposta'] = resposta 
    
    return render(request, 'eventos_form.html', context)

def deleteEventos(request,idauxiliar):
    url1 = 'http://localhost:3000/listAll'
    url = ''
    headers={'Content-Type': 'application/json'} 
    response = requests.get(url1, headers= headers)
    response = json.loads(response.content)
    eventos = response
    
    for x in eventos:
        if x['id_auxiliar'] == idauxiliar:
            url = f"http://127.0.0.1:3000/deletar/{x['_id']}"
    
    response = requests.delete(url)
    return redirect('/dashboard/eventosDisponiveis')

def Publico_eventos(request, idauxiliar, idpublico):
    url3 = 'http://127.0.0.1:3000/listallpe'
    url = 'http://127.0.0.1:3000/api-publico_eventos'
            
    response = requests.get(url3)
    response = json.loads(response.content)      
    for x in response:
        if x['id_publico'] == idpublico and x['id_evento'] == idauxiliar:
            messages.error(request, 'Você já fez uma reserva para este evento!')
            return redirect('/dashboard/eventosDisponiveis')
    
    pe_data = {
        'id_publico' : idpublico,
        'id_evento': idauxiliar,
    }
    response = requests.post(url = url, json = pe_data)
    messages.success(request, 'Participação concluída, fique atento ao dia e horário do seu evento.')
        
    return redirect('/dashboard/suasReservas')
           
def deletePublicoEventos(request, idauxiliar, idpublico):
    url2 = 'http://127.0.0.1:3000/listallpe/'
    response = requests.get(url2)
    response = json.loads(response.content)
    
    for x in response:
        if x['id_publico'] == idpublico and x['id_evento'] == idauxiliar:
            idpe = x['_id']
            apagar = requests.delete(f'http://127.0.0.1:3000/deletarpe/{idpe}/')
    return redirect('/dashboard/suasReservas')


# SERIALIZAR DADOOS PARA API    
class PublicoViewSet(viewsets.ModelViewSet):
    queryset = PublicoGeral.objects.all()
    serializer_class = PublicoSerializer

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimentos.objects.all()
    serializer_class = EstabelecimentoSerializer
    
def baixarPdf(request, idauxiliar):
    headers={'Content-Type': 'application/json'} 
    url3 = 'http://localhost:3000/listAll'
    evento = ''
    
    response = requests.get(url3,headers = headers)
    response   = json.loads(response.content)
    eventos = response
    for x in eventos:
        if x['id_auxiliar'] == idauxiliar:
            evento = x
    
    url2 = 'http://127.0.0.1:3000/listallpe/'
    
    response = requests.get(url2)
    response = json.loads(response.content)
    list_aux=[]
    
    for x in response:
        if x['id_evento'] == idauxiliar:
            list_aux.append(x['id_publico'])
    
    listaPessoas = []
    
    for x in list_aux:
        if PublicoGeral.objects.filter(pk = x):
            listaPessoas.append(PublicoGeral.objects.get(pk = x))

    data = {'evento': evento, 'pessoas':listaPessoas}

    pdf = render_to_pdf('../templates/arquivoPDF.html', data)

    if pdf:
        response = HttpResponse(pdf, content_type='application/pdf')

        filename = ' Listagem de pessoas em {}.pdf'.format(evento['titulo'])

        #content = "inline; filename='%s'" %(filename)
        #download = request.GET.get("download")
        #if download:
        content = 'attachment; filename=%s' %(filename)
        response['Content-Disposition'] = content
        return response
    else:
        return HttpResponse("Not found")

