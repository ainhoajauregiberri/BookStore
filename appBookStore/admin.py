from django.contrib import admin

# Register your models here.

from .models import Autor, Genero, Editorial, Idioma, Libro
admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Editorial)
admin.site.register(Idioma)
admin.site.register(Libro)

