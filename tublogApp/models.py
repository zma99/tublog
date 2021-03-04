from django.db import models

class Usuario(models.Model):
    usuario = models.CharField(max_length=15, primary_key=True, unique=True)
    contrasenia = models.CharField (max_length=10)
    email = models.EmailField(max_length=20, unique=True)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    fecha_nacimiento = models.DateField(auto_now=False, auto_now_add=False)
    direccion = models.CharField(max_length=50)
    ciudad = models.CharField(max_length=15)
    provincia = models.CharField(max_length=15)


class Posteo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    titulo = models.CharField(max_length=20)
    objeto_panel = models.Manager()
    comentario = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to = 'photos')
   


class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=20, unique=True)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    mensaje = models.CharField(max_length=150)
