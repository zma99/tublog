from django.contrib import admin
from .models import Comentario, Post, Contacto


admin.site.register(Comentario)
admin.site.register(Post)
admin.site.register(Contacto)