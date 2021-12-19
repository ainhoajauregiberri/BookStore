from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Autor, Genero, Idioma, Editorial, Libro, Usuario


#devuelve el usuario que ha iniciado sesion
def inicio(request):
	usuarios = get_list_or_404(Usuario.objects.order_by('id'))
	context = {'usuarios': usuarios}
	return render(request, 'inicio.html', context)

#devuelve el listado de libros de cada editorial
def index(request, usuario_id):
	editorial1 = Editorial.objects.get(pk=1)
	librosEd1 = editorial1.libro_set.all()
	librosEd1 = librosEd1.order_by('fechaPubli').reverse()

	editorial2 = Editorial.objects.get(pk=2)
	librosEd2 = editorial2.libro_set.all()
	librosEd2 = librosEd2.order_by('fechaPubli').reverse()

	
	context = {'libro1': librosEd1[0], 'libro2': librosEd2[0], 'usuario':usuario_id}
	return render(request, 'index.html', context)

#devuelve la lista de LIBROS
def listaLibros(request, usuario_id):
	libros = get_list_or_404(Libro.objects.order_by('id'))
	context = {'lista_libros' : libros, 'usuario':usuario_id}
	return render(request, 'listaLibros.html', context)

#devuelve los detalles de un LIBRO
def detallesLibro(request, libro_id, usuario_id):
	libro = get_object_or_404(Libro, pk=libro_id)
	autores = libro.autores.all()
	context = {'libro' : libro, 'autores' : autores, 'usuario':usuario_id}
	return render(request, 'detallesLibro.html', context)


#devuelve la lista de EDITORIALES
def listaEditoriales(request, usuario_id):
	editoriales = get_list_or_404(Editorial.objects.order_by('id'))
	context = {'lista_editoriales' : editoriales, 'usuario':usuario_id}
	return render(request, 'listaEditoriales.html', context)	

#devuelve los detalles de EDITORIALES
def detallesEditoriales(request, editorial_id, usuario_id):
	editorial = get_object_or_404(Editorial, pk=editorial_id)
	libros = editorial.libro_set.all()
	context = {'editorial' : editorial, 'libros' : libros, 'usuario':usuario_id}
	return render(request, 'detallesEditorial.html', context)

#devuelve la lista de AUTORES
def listaAutores(request, usuario_id):
	autores = get_list_or_404(Autor.objects.order_by('id'))
	context = {'lista_autores' : autores, 'usuario':usuario_id}
	return render(request, 'listaAutores.html', context)	

#devuelve los detalles de los AUTORES
def detallesAutores(request, autor_id, usuario_id):
	autor = get_object_or_404(Autor, pk=autor_id)
	libros = autor.libro_set.all()
	context = {'autor' : autor, 'libros': libros, 'usuario':usuario_id}
	return render(request, 'detallesAutor.html', context)