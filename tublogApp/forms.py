from django import forms
from .models import Contacto

    
class formContacto(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = '__all__'