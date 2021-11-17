from django.db import migrations, models


import django.utils.datetime_safe
from django.db.models.fields import FloatField

from datetime import timezone
 
class Autor(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.id}. {self.nombre}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
# Campo para la relación one-to-many
    def __str__(self):
        return f"{self.id}. {self.nombre}"
	

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
# Campo para la relación one-to-many
    def __str__(self):
        return f"{self.id}. {self.nombre}"


class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
# Campo para la relación one-to-many
    def __str__(self):
        return f"{self.id}. {self.nombre}"

class Libro(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    paginas = models.IntegerField(default=0)
    sinopsis = models.CharField(max_length=800)
    def __str__(self):
        return f"{self.id}. {self.nombre}, {self.autores.all()}, {self.editorial}, {self.genero}, {self.idioma}, {self.paginas} páginas"




 


 
