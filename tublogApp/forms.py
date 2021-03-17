from django import forms
from .models import Contacto
from django.contrib.auth.forms import UserCreationForm

    
class formContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'


class nuevoUsuario(UserCreationForm):
    pass