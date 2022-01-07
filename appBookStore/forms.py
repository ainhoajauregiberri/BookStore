from .models import Usuario
from django import forms

class UsuarioForm(forms.ModelForm):    
    class Meta:
        model = Usuario
        fields = ("__all__")
        exclude = ['notificar']