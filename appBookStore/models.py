from django.db import migrations, models


import django.utils.datetime_safe
from django.db.models.fields import FloatField

 
class Autor(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    def __str__(self):
        return f"id={self.id}, nombre{self.nombre}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
# Campo para la relación one-to-many
    def __str__(self):
        return f"id={self.id}, nombre{self.nombre}"
	

class Genero(models.Model):
    nombre = models.CharField(max_length=50)
# Campo para la relación one-to-many
    def __str__(self):
        return f"id={self.id}, nombre{self.nombre}"


class Idioma(models.Model):
    nombre = models.CharField(max_length=50)
# Campo para la relación one-to-many
    def __str__(self):
        return f"id={self.id}, nombre{self.nombre}"

class Libro(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    autores = models.ManyToManyField(Autor)
    editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
    paginas = models.IntegerField(default=0)
    def __str__(self):
        return f"id={self.id}, nombre={self.nombre}, autores={self.autores.all()}, editorial={self.editorial}, genero={self.genero}, idioma={self.idioma}, paginas={self.paginas}"




 


 
