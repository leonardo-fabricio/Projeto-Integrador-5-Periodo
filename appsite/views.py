
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib import messages
from appsite.models import PublicoGeral
from rest_framework import viewsets
from appsite.serializer import *
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from .utils import *

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
            seus_eventos = Eventos.objects.filter(id_estabelecimento = id_user)
               
    eventos = Eventos.objects.all()
    countEventos = Eventos.objects.count()

    peventos = Publico_Eventos.objects.select_related('idEvento').filter(idPessoa = iduser)
    countEventosPessoa = peventos.count()
                 
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

# SERIALIZAR DADOOS PARA API    
class PublicoViewSet(viewsets.ModelViewSet):
    queryset = PublicoGeral.objects.all()
    serializer_class = PublicoSerializer

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Eventos.objects.all()
    serializer_class = EventoSerializer
    
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

