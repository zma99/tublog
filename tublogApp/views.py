from django.shortcuts import render, redirect
from .forms import formRegistro, formContacto
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def inicio(request):
    
    return render(request, 'inicio.html')


def posteos(request):
    
    return render(request, 'posteos.html')


def noticias(request):
    
    return render(request, 'noticias.html')


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


def registrar(request):

    if request.method == 'GET':
        formulario = formRegistro()
        contexto = { 'formulario':formulario }

    if request.method == 'POST':
        formulario = formRegistro(request.POST)
        print(formulario)
        contexto = { 'formulario':formulario }

    if formulario.is_valid():
        formulario.save()
        return redirect('inicio')

    return render(request, 'registrar.html', contexto)

def login(request):
    
    return render(request, 'login.html')

