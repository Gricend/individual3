from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
# Create your views here.

def landing(request):
    return render(request, 'landing.html')

def formulario_contacto(request):
    return render(request, 'contacto.html')

def lista_usuario(request) -> HttpResponse:
    users = User.objects.all()
    return render(request, 'usuarios.html', {'users': users})