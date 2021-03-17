from django.db import models
from django.contrib.auth.models import User


class Comentario(models.Model):
    id = models.AutoField(primary_key=True)
    contenido = models.TextField('Comentario', max_length=150, default="", null=False, blank=False)

    class Meta:
        verbose_name = 'Comentario'
        verbose_name_plural = 'Comentarios'

    def __str__(self):
        return self.id

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(User, default="", null=False, blank=False, on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=50, default="", null=False, blank=False)
    descripcion = models.TextField('Descripción', max_length=1000, default="", null=True, blank=True)
    imagen = models.ImageField(upload_to='posteos/')
    fecha_creacion = models.DateField('Fecha de creación', auto_now=False, auto_now_add=True)
    #like = models.IntegerField(default=0)
    #cantidad_comentarios = models.IntegerField(default=0)
    #id_comentario = models.ForeignKey(Comentario, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posteos'

    def __str__(self):
        return self.titulo


class Contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField('Nombre', default="", max_length=50, null=False, blank=False)
    apellido = models.CharField('Apellido', default="", max_length=50, null=False, blank=False)
    email = models.EmailField('Email', null=False, blank=False)
    asunto = models.CharField('Asunto', default="", max_length=50, null=False, blank=False)
    mensaje = models.TextField('Mensaje', default="", max_length=500, null=False, blank=False)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'

    def __str__(self):
        return self.email
