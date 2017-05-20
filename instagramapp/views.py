from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'Inst.html')


def crear_usuario(request):
    print (request.POST[ 'email' ])
    print (request.POST[ ' username' ])
