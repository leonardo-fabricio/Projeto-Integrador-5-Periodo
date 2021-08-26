
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from .forms import *
from django.contrib import messages
from .models import *
from django.contrib import messages

# Create your views here.
def index(request):
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
                tipoUsuario = x.tipoUsuario
                # print(tipoUsuario)
        else:
            usuario = Estabelecimentos.objects.filter(email=request.user.email)
            print('\n\n\n\n\n')
            for x in usuario:
                tipoUsuario = x.tipoUsuario
                # print(tipoUsuario)
            id_user = get_object_or_404(Estabelecimentos,email = request.user.email)
            seus_eventos = Eventos.objects.filter(id_estabelecimento = id_user)
            
    eventos = Eventos.objects.all()
                 
    content = {
        'tipoUsuario' : tipoUsuario,
        'eventos' : eventos,
        'seus_eventos' : seus_eventos,
    }
    
    return render(request, 'eventosDisponiveis.html', content) 

def cadastroEstabelecimento(request):
    form = EstabelecimentoModel(request.POST or None)
    if form.is_valid():
        nome   = form.cleaned_data['nome']
        tipo   = form.cleaned_data['tipo']
        rua    = form.cleaned_data['rua']
        cep    = form.cleaned_data['cep']
        cidade = form.cleaned_data['cidade']
    
        if Estabelecimentos.objects.filter(email = request.user.email):
            Estabelecimentos.objects.filter(email = request.user.email).update(nome = nome, tipo= tipo, rua = rua, cep = cep, cidade = cidade)
        else:
            new = Estabelecimentos(nome = nome,tipo = tipo, rua = rua, cep = cep, cidade = cidade, email = request.user.email, tipoUsuario = 'estabelecimento')
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
        
        form = CriarEventoModel(request.POST, request.FILES)
        
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

                messages.success(request, 'Evento cadastrado com sucesso!')
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
    }
    return render(request, 'criarEvento.html', context)
   
def cadastroPublico(request):
    form = PublicoModel(request.POST or None)
    if str(request.method) == 'POST' : 
        if form.is_valid():
            cidade   = form.cleaned_data['cidade']
            telefone = form.cleaned_data['telefone'] # eu sei 
            if PublicoGeral.objects.filter(email = request.user.email):
                PublicoGeral.objects.filter(email = request.user.email).update(telefone = telefone, cidade = cidade)
            else:
                if request.user.get_full_name != '':
                    new = PublicoGeral(nome = request.user.first_name, cidade = cidade, telefone = telefone, email = request.user.email, tipoUsuario = 'normal')
                    # new.save() isso so precisa inserir uma vez po 
                else:
                    new = PublicoGeral(nome = request.username, cidade = cidade, telefone = telefone, email = request.user.email, tipoUsuario = 'normal')
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
        if PublicoGeral.objects.filter(email = request.user.email):
            usuario = PublicoGeral.objects.filter(email = request.user.email)
            for x in usuario:
                tipoUsuario = x.tipoUsuario
        else:
            usuario = Estabelecimentos.objects.filter(email = request.user.email)
            for x in usuario:
                tipoUsuario = x.tipoUsuario
            
    content = {
        'tipoUsuario' : tipoUsuario
    }
    return render(request, 'suasReservas.html',content)

def escolha(request): 
    return render(request, 'escolha.html')

def deleteEventos(request, id):
    eventodelete = get_object_or_404(Eventos, pk=id)
    eventodelete.delete()
    return redirect('/dashboard/eventosDisponiveis')
    
