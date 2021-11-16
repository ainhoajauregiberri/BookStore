from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Autor, Genero, Idioma, Editorial, Libro


#devuelve el listado de libros de cada editorial
def index(request):
	editorial1 = Editorial.objects.get(pk=1)
	librosEd1 = editorial1.libro_set.all()
	librosEd1 = librosEd1.order_by('id')

	editorial2 = Editorial.objects.get(pk=2)
	librosEd2 = editorial2.libro_set.all()
	librosEd2 = librosEd2.order_by('id')

	
	context = {'libro1': librosEd1, 'libro2': librosEd2}
	return render(request, 'index.html', context)

#devuelve la lista de LIBROS
def listaLibros(request):
	libros = get_list_or_404(Libro.objects.order_by('id'))
	context = {'lista_libros' : libros}
	return render(request, 'listaLibros.html', context)

#devuelve los detalles de un LIBRO
def detallesLibro(request, libro_id):
	libro = get_object_or_404(Libro, pk=libro_id)
	autores = libro.autores.all()
	context = {'libro' : libro, 'autores' : autores}
	return render(request, 'detallesLibro.html', context)


#devuelve la lista de EDITORIALES
def listaEditoriales(request):
	editoriales = get_list_or_404(Editorial.objects.order_by('id'))
	context = {'lista_editoriales' : editoriales}
	return render(request, 'listaEditoriales.html', context)	

#devuelve los detalles de EDITORIALES
def detallesEditoriales(request, editorial_id):
	editorial = get_object_or_404(Editorial, pk=editorial_id)
	libros = editorial.libro_set.all()
	context = {'editorial' : editorial, 'libros' : libros}
	return render(request, 'detallesEditorial.html', context)

#devuelve la lista de AUTORES
def listaAutores(request):
	autores = get_list_or_404(Autor.objects.order_by('id'))
	context = {'lista_autores' : autores}
	return render(request, 'listaAutores.html', context)	

#devuelve los detalles de los AUTORES
def detallesAutores(request, autor_id):
	autor = get_object_or_404(Autor, pk=autor_id)
	libros = autor.libro_set.all()
	context = {'autor' : autor, 'libros': libros}
	return render(request, 'detallesAutor.html', context)