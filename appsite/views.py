from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'index.php')

def login(request):
    return render(request, 'login.php')

# def teste (request):
#     return render(request, 'teste.php')