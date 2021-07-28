from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'index.php')

# def teste (request):
#     return render(request, 'teste.php')