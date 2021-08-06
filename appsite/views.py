
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .forms import EstabelecimentoModel,EstabelecimentoForm
from django.contrib import messages
from .models import Estabelecimentos

# Create your views here.
def index (request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'index.html', {})

def login(request):
    return render(request, 'login.html')
# def teste (request):
#     return render(request, 'teste.php')
def logout(request):
    return LogoutView.as_view()

def profile(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'profile.html', {})

def dashboard(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/')
    return render(request, 'dashboard.html', {})

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
            return redirect('/profile')
  
    context = {
        'form' : form,
        'email': email
    }
    return render(request,'cadastroEstabelecimento.html',context)