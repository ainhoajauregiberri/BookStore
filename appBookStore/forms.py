from BookStore.appBookStore.models import Valoracion
from .models import Usuario
from django import forms

class UsuarioForm(forms.ModelForm):    
    class Meta:
        model = Usuario
        fields = ("__all__")
        exclude = ['notificar']

class UsuariosExistentesForm(forms.ModelForm):    
    class Meta:
        model = Usuario
        fields = ("__all__")
        exclude = ['notificar', 'nombre']

class CrearValoracion(forms.ModelForm):    
    class Meta:
        model = Valoracion
        fields = ("__all__")
        exclude = ['puntuacion']

        