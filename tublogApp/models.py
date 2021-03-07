from django.db import models

'''class Usuario(models.Model):
    correo = models.EmailField(primary_key=True)
    contrasenia = models.CharField(max_length=30)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()
    pais = models.CharField(max_length=20)
    foto_perfil = models.ImageField(blank=True,null=True)

    def __str__(self):
        return self.correo


class Post(models.Model):
    titulo = models.CharField(max_length=30)
    descripcion = models.TextField()
    imagen = models.ImageField(blank=True,null=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    actualizacion = models.DateTimeField(auto_now=True)
    #autor = models.ForeingKey()

    def __str__(self):
        return self.titulo'''
