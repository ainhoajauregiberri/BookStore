from django.contrib import admin
from .models import Autor, Genero, Editorial, Idioma, Libro, Usuario, Valoracion

# Register your models here.


'''class LibroAdmin(admin.ModelAdmin):
    actions = ['addNotificarLibro']
    def addNotificarLibro(self, request, queryset):
        for usuario in queryset:
            usuario.notificacion = True
            usuario.save()'''

admin.site.register(Autor)
admin.site.register(Genero)
admin.site.register(Editorial)
admin.site.register(Idioma)
admin.site.register(Libro)
admin.site.register(Usuario)
admin.site.register(Valoracion)






