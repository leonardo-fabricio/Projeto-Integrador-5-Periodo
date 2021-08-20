
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
def index (request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html')
   
def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'profile.html', {})

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'eventosDisponiveis.html', {})

def cadastroEstabelecimento(request, email):
    form = EstabelecimentoModel(request.POST or None)
    if str(request.method) == 'POST' :
        if form.is_valid():
            nome = form.cleaned_data['nome']
            tipo = form.cleaned_data['tipo']
            rua = form.cleaned_data['rua']
            cep = form.cleaned_data['cep']
            cidade = form.cleaned_data['cidade']
            if(Estabelecimentos.objects.filter(email = email)):
                Estabelecimentos.objects.filter(email = email).update(nome = nome,tipo = tipo, rua = rua, cep = cep, cidade = cidade)
            else:
                new = Estabelecimentos(nome = nome,tipo = tipo, rua = rua, cep = cep, cidade = cidade, email = email)
                new.save()
            
            form = EstabelecimentoForm()
            return redirect('/dashboard')
  
    context = {
        'form' : form,
        'email': email
    }
    return render(request,'cadastroEstabelecimento.html',context)

def criarEvento(request,email):
    form = CriarEventoModel(request.POST or None)
    
    if str(request.method) == 'POST':
        if form.is_valid():
            qtdPessoas  = form.cleaned_data['qtdPessoas']
            horaInicial = form.cleaned_data['horaInicial']
            horaFinal   = form.cleaned_data['horaFinal']
            local       = form.cleaned_data['local']
            dataEvento  = form.cleaned_data['dataEvento']
            # imagem      = form.cleaned_data['Imagem']

            id_user = get_object_or_404(PublicoGeral,email = email)
            new = Eventos(qtdPessoas = qtdPessoas, horaInicial = horaInicial, horaFinal = horaFinal,local = local,dataEvento = dataEvento,id_estabelecimento=id_user)

            messages.success(request, 'Evento cadastrado com sucesso!')
            new.save()
            form = CriarEventoForm()

            # print(f'QTD PESSOA: {qtdpessoas}')
            # print(f'Image: {imagem}')

        else:
            messages.error(request, 'Erro ao cadastrar evento!')
    context ={
        'form': form,
        'email': email,
    }
    return render(request, 'criarEvento.html', context)
   
def cadastroPublico(request, email):
    form = PublicoModel(request.POST or None)
    if str(request.method) == 'POST' :
        if form.is_valid():
            nome     = form.cleaned_data['nome']
            cidade   = form.cleaned_data['cidade']
            telefone = form.cleaned_data['telefone']
            if PublicoGeral.objects.filter(email = email):
                PublicoGeral.objects.filter(email = email).update(telefone = telefone, cidade = cidade)
            else:
                new = PublicoGeral(nome = nome, cidade = cidade, telefone = telefone, email = email)
                new.save()
            
            form = EstabelecimentoForm()
            return redirect('/dashboard/eventosDisponiveis')
  
    context = {
        'form' : form,
        'email' : email
    }
    return render(request, 'cadastroPublico.html',context)

def suasReservas(request): 
    return render(request, 'suasReservas.html')