from django.contrib import admin
from .models import Usuario, Comentario, Posteo, Contacto

admin.site.register(Usuario)
admin.site.register(Comentario)
admin.site.register(Posteo)
admin.site.register(Contacto)