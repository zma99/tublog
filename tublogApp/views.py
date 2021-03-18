from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate
from .forms import formContacto, nuevoUsuario
from .models import Post


def base(request):

    return inicio(request)

def inicio(request):
    posteos = Post.objects.all()
    contexto = {
        'posteos':posteos
    }
    return render(request, 'inicio.html', contexto)


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



def registro(request):
    contexto = {
        'form':nuevoUsuario()
    }

    if request.method == 'GET':
        formulario = nuevoUsuario()

    if request.method == 'POST':
        formulario = nuevoUsuario(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to='inicio')
            

    return render(request, 'registration/registro.html', contexto)


def perfil(request):
    usuario = user.username
    return render(request, 'perfil.html')
