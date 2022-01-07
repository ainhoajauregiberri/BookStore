from django.db import migrations, models
from django.db.models.lookups import In


import django.utils.datetime_safe
from django.db.models.fields import FloatField, IntegerField

from datetime import timezone
 
class Autor(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    biografia = models.CharField(max_length=800)
    imagenLink = models.CharField(max_length=800)
    def __str__(self):
        return f"{self.id}. {self.nombre}"

class Editorial(models.Model):
    nombre = models.CharField(max_length=50)
    explicacion = models.CharField(max_length=800)
    imagenLink = models.CharField(max_length=800)
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
    fechaPubli = models.DateField()
    mediaValoracion = models.FloatField(default=0)
    numValoraciones = models.IntegerField(default=0)
    imagenLink = models.CharField(max_length=800)
    def linkLibro(self):
        return f"fotos/{self.id}.jpg"
    def __str__(self):
        return f"{self.id}. {self.nombre}, {self.autores.all()}, {self.editorial}, {self.genero}, {self.idioma}, {self.paginas} páginas"

class Usuario(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    nombre = models.CharField(max_length=50)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    notificar = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.id}. {self.usuario}. {self.password}"

class Valoracion(models.Model):
 # No es necesario crear un campo para la Primary Key, Django creará automáticamente un IntegerField.
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    puntuacion = models.IntegerField(default=0)
    texto = models.CharField(max_length=1000, default="")
    def __str__(self):
        return f"{self.usuario}: {self.puntuacion} ({self.libro})"


 


 
