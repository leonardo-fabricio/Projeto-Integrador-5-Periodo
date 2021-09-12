
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from .models import *
from django.contrib import messages
from rest_framework import viewsets
from appsite.serializer import *
from reportlab.lib.pagesizes import A4
from .utils import *
import requests
import json

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
            id_user = get_object_or_404(Estabelecimentos,email = request.user.email)
            
            # seus_eventos = Eventos.objects.filter(id_estabelecimento = id_user)
    
    url = 'http://localhost:1010/api-evento/'     
    headers={'Content-Type': 'application/json'} 
    response = requests.get(url, headers= headers)
    
    response = json.loads(response.content)
    
    eventos = response
    # for x in eventos:
    #     print(x['titulo'])
    
    print(f'\n\n\neventos:{eventos}\n\n\n')
    # countEventos = Eventos.objects.count()

    # peventos = Publico_Eventos.objects.select_related('idEvento').filter(idPessoa = iduser)
    # countEventosPessoa = peventos.count()
                 
    content = {
        'tipoUsuario' : tipoUsuario,
        'eventos' : eventos,
        # 'seus_eventos' : seus_eventos,
        'foto' : foto,
        'iduser': iduser,
        'nomeEsta' : nome,
        # 'countEventos': countEventos,
        # 'countEventosPessoa': countEventosPessoa,
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
       
    peventos = Publico_Eventos.objects.select_related('idEvento').filter(idPessoa = iduser)
    countEventos = Eventos.objects.count()
    countEventosPessoa = peventos.count()

    # for x in peventos:
    #     print (x.idEvento.titulo)
    #     print('\n\n')
    
    
    # print(eventosReservados.query)
    # print('\n\n\n')
    # print (eventos)
    # print('\n\n')
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

# SERIALIZAR DADOOS PARA API    
class PublicoViewSet(viewsets.ModelViewSet):
    queryset = PublicoGeral.objects.all()
    serializer_class = PublicoSerializer

class EstabelecimentoViewSet(viewsets.ModelViewSet):
    queryset = Estabelecimentos.objects.all()
    serializer_class = EstabelecimentoSerializer
    
def baixarPdf(request, idevento):
        evento          = Eventos.objects.get(id = idevento)
        listaPessoas    = Publico_Eventos.objects.select_related('idPessoa').filter(idEvento = idevento)
        data = {'evento': evento, 'pessoas':listaPessoas}

        #html = template.render(data)
        pdf = render_to_pdf('../templates/arquivoPDF.html', data)

        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')

            filename = ' Listagem de pessoas em {}.pdf'.format(evento.titulo)

            #content = "inline; filename='%s'" %(filename)
            #download = request.GET.get("download")
            #if download:
            content = 'attachment; filename=%s' %(filename)
            response['Content-Disposition'] = content
            return response
        else:
            return HttpResponse("Not found")

