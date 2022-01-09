from django.db.models import fields
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
        db_constraints = {
            'puntuacion': 'check (puntuacion<6)'
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['puntuacion'].widget.attrs.update({
            'class': 'form-puntuacion'
        })
        self.fields['texto'].widget.attrs.update({
            'class': 'form-texto'
        })

#class CrearValoracion(forms.ModelForm):    
 #   class Meta:
  #      model = Valoracion
   #     fields = ("__all__")
    #    exclude = ['puntuacion']

        