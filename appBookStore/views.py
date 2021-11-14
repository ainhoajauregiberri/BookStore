from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render
from .models import Autor, Genero, Idioma, Editorial, Libro


#devuelve el listado de libros de cada editorial
def index(request):
	editorial1 = Editorial.objects.get(pk=1)
	librosEd1 = editorial1.libro_set.all()
	librosEd1 = librosEd1.order_by('nombre')

	editorial2 = Editorial.objects.get(pk=2)
	librosEd2 = editorial2.libro_set.all()
	librosEd2 = librosEd2.order_by('nombre')
	
	output = ', '.join([str(librosEd1[0].id), str(librosEd1[0].nombre), str(librosEd1[0].editorial), str([a.nombre for a in librosEd1[0].autores.all()]), str(librosEd2[0].id), str(librosEd2[0].nombre), str(librosEd2[0].editorial), str([a.nombre for a in librosEd2[0].autores.all()])])
	return HttpResponse(output)

#devuelve la lista de LIBROS
def listaLibros(request):
	libros = Libro.objects.order_by('id')
	context = {'lista_libros' : libros}
	return render(request, 'listaLibros.html', context)

#devuelve los detalles de un LIBRO
def detallesLibro(request, libro_id):
	libro = Libro.objects.get(pk=libro_id)
	output = ', '.join([str(libro.id), libro.nombre, str(libro.editorial), str([a.nombre for a in libro.autores.all()])])
	return HttpResponse(output)


#devuelve la lista de EDITORIALES
def listaEditoriales(request):
	editoriales = Editorial.objects.order_by('id')
	context = {'lista_editoriales' : editoriales}
	return render(request, 'listaEditoriales.html', context)	

#devuelve los detalles de EDITORIALES
def detallesEditoriales(request, editorial_id):
	editorial = Editorial.objects.get(pk=editorial_id)
	output = ', '.join([str(editorial.id), editorial.nombre, str([l.nombre for l in editorial.libro_set.all()])])
	return HttpResponse(output)

#devuelve la lista de AUTORES
def listaAutores(request):
	autores = Autor.objects.order_by('id')
	context = {'lista_autores' : autores}
	return render(request, 'listaAutores.html', context)	

#devuelve los detalles de los AUTORES
def detallesAutores(request, autor_id):
	autor = Autor.objects.get(pk=autor_id)
	output = ', '.join([str(autor.id), autor.nombre, str([l.nombre for l in autor.libro_set.all()])])
	return HttpResponse(output)