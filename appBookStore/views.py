from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Autor, Genero, Idioma, Editorial, Libro


#devuelve el listado de libros de cada editorial
def index(request):
	librosEd1 = Libro.objects.get(editorial_id=1)
	librosEd1 = librosEd1.order_by('nombre')
	
	librosEd2 = Libro.objects.get(editorial_id=2)
	librosEd2 = librosEd2.order_by('nombre')
	output = ', '.join(librosEd1[0], librosEd2[0])
	return HttpResponse(output)

#devuelve la lista de LIBROS
def listaLibros(request):
	libros = Libro.objects.order_by('nombre')
	output = ', '.join([l.nombre for l in libros])
	return HttpResponse(output)	

#devuelve los detalles de un LIBRO
def detallesLibro(request, libro_id):
	libro = Libro.objects.get(pk=libro_id)
	output = ', '.join([str(libro.id), libro.nombre, str(libro.editorial), str([a.nombre for a in libro.autores.all()])])
	return HttpResponse(output)

#devuelve la lista de EDITORIALES
def listaEditoriales(request):
	editoriales = Editorial.objects.order_by('nombre')
	output = ', '.join([e.nombre for e in editoriales])
	return HttpResponse(output)		

#devuelve los detalles de EDITORIALES
def detallesEditoriales(request, editorial_id):
	editorial = Editorial.objects.get(pk=editorial_id)
	output = ', '.join([str(editorial.id), editorial.nombre, str([l.nombre for l in editorial.libro_set.all()])])
	return HttpResponse(output)

#devuelve la lista de AUTORES
def listaAutores(request):
	autores = Autor.objects.order_by('nombre')
	output = ', '.join([a.nombre for a in autores])
	return HttpResponse(output)	

#devuelve los detalles de los AUTORES
def detallesAutores(request, autor_id):
	autor = Autor.objects.get(pk=autor_id)
	output = ', '.join([str(autor.id), autor.nombre, str([l.nombre for l in autor.libro_set.all()])])
	return HttpResponse(output)