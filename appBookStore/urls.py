from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('getDatosUsuario/', views.getDatosUsuario, name='getDatosUsuario'),
    path('iniciarSesionUsuario/', views.iniciarSesionUsuario, name='iniciarSesionUsuario'),

    path('index/', views.index, name='index'),
    

    path('libro/', views.listaLibros, name='listaLibros'),
    path('libro/<int:libro_id>/autores/', views.detallesLibro, name='detallesLibro'),

    path('editorial/', views.listaEditoriales, name='listaEditoriales'),
    path('editorial/<int:editorial_id>/libros/', views.detallesEditoriales, name='detallesEditoriales'),

    path('autor/', views.listaAutores, name='listaAutores'),
    path('autor/<int:autor_id>/libros/', views.detallesAutores, name='detallesAutores'),

]