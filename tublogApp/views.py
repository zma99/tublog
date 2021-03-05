from django.shortcuts import render


def inicio(request):
    
    return render(request, 'inicio.html')


def posteos(request):
    
    return render(request, 'posteos.html')


def noticias(request):
    
    return render(request, 'noticias.html')


def nosotros(request):
    
    return render(request, 'nosotros.html')


def contacto(request):
    
    return render(request, 'contacto.html')

def registrar(request):

    return render(request, 'registrar.html')