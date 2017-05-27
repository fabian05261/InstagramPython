from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from instagramapp.models import *# Create your views here.

def login(request):
    return render(request, 'login.html')
    
def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'Inst.html')


def crear_usuario(request):
    _email = (request.POST[ 'email' ])
    _username = (request.POST[ 'username' ])
    _name = (request.POST[ 'name' ])
    _password = (request.POST[ 'password' ])
    user=User.objects.create_user( username = _username, email =_email, first_name =_name, password= _password  )
    myUser = MiUsuario ( usuario = user )
    myUser.save()
    return redirect('login')
