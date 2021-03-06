from django.contrib import admin
from .models import Usuario, Posteo, Contacto, Comentario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Posteo)
admin.site.register(Contacto)
