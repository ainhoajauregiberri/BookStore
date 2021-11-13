from django.db import models
from django.db.models.fields import FloatField
 
class Autor(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombre = models.CharField(max_length=50)

class Editorial(models.Model):
 nombre = models.CharField(max_length=50)
# Campo para la relación one-to-many

class Genero(models.Model):
 nombre = models.CharField(max_length=50)
# Campo para la relación one-to-many

class Idioma(models.Model):
 nombre = models.CharField(max_length=50)
# Campo para la relación one-to-many

class Libro(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
 nombre = models.CharField(max_length=50)
 autores = models.ManyToManyField(Autor)
 editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
 genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
 idioma = models.ForeignKey(Idioma, on_delete=models.CASCADE)
 paginas = models.IntegerField(default=0)



 


 
