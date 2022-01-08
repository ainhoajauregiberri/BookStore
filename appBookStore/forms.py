from django.db.models import fields

from BookStore.appBookStore.models import Libro
from .models import Usuario
from .models import Valoracion
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

class ValoracionCrear(forms.ModelForm):
    class Meta:
        model = Valoracion
        fields = ['puntuacion', 'texto']
        
#class CrearValoracion(forms.ModelForm):    
 #   class Meta:
  #      model = Valoracion
   #     fields = ("__all__")
    #    exclude = ['puntuacion']

        