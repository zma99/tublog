from django.db import models
from datetime import datetime, date
from django.utils import timezone


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=20)
    descripcion = models.TextField(blank=True)
    objeto_panel = models.Manager()
    imagen = models.ImageField(upload_to = 'photos')
    id_comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE, default=None)
    fecha_publicacion = models.DateTimeField(default=timezone.now)


class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    nombre = models.CharField(max_length=10)
    apellido = models.CharField(max_length=15)
    mensaje = models.TextField(blank=True)
    objeto_panel = models.Manager()

    def __str__(self):
        return self.email