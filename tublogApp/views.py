from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from .forms import formContacto

def base(request):

    return inicio(request)

def inicio(request):
    
    return render(request, 'inicio.html')


@login_required
def postear(request):
    
    return render(request, 'postear.html')


def nosotros(request):
    
    return render(request, 'nosotros.html')


def contacto(request):

    if request.method == 'GET':
        formulario = formContacto()
        contexto = { 'formulario':formulario }

    if request.method == 'POST':
        formulario = formContacto(request.POST)
        print(formulario)
        contexto = { 'formulario':formulario }

    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')
    
    return render(request, 'contacto.html', contexto)

