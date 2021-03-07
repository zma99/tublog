from django import forms
from .models import Usuario, Contacto

class formRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
    
class formContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'