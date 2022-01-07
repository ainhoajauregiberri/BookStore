from django.db.models import fields
from .models import Usuario
from django import forms
from .models import Valoracion

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

class ValoracionCrear(forms.Valoracion):
    class Meta:
        model = Valoracion
        fields = ['puntuacion', 'texto']


#class CrearValoracion(forms.ModelForm):    
 #   class Meta:
  #      model = Valoracion
   #     fields = ("__all__")
    #    exclude = ['puntuacion']

        