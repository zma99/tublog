from django import forms
from .models import Usuario

class formRegistro(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = '__all__'
    
    '''correo = forms.EmailField()
    contrasenia = forms.CharField()
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    fecha_nacimiento = forms.DateField()
    pais = forms.CharField(max_length=20)
    foto_perfil = forms.ImageField()'''