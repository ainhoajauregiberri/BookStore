from django.http import HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render

from appBookStore.forms import UsuarioForm
from .models import Autor, Genero, Idioma, Editorial, Libro, Usuario

from pprint import pprint

#devuelve el usuario que ha iniciado sesion
def inicio(request):
	usuarios = get_list_or_404(Usuario.objects.order_by('id'))
	context = {'usuarios': usuarios}
	return render(request, 'inicio.html', context)

#devuelve el usuario que ha iniciado sesion
def registrarse(request):
	form = UsuarioForm()
	context = {'form' : form}
	return render(request, 'registrarse.html', context)
    
def getDatosUsuario(request):
	if request.method=='POST':
		form= UsuarioForm(request.POST)
		if form.is_valid():
			nombre = form.cleaned_data['nombre']

			pprint(dir(Usuario))

			usuario = form.cleaned_data['usuario']
			password = form.cleaned_data['password']
			usuarioCreado = Usuario(20, nombre, usuario, password)
			usuarioCreado.save()
			return HttpResponseRedirect('../')
	else:
		form = UsuarioForm()
	return render(request, 'registrarse.html', {'form' : form})








#devuelve el listado de libros de cada editorial
def index(request):
	editorial1 = Editorial.objects.get(pk=1)
	librosEd1 = editorial1.libro_set.all()
	librosEd1 = librosEd1.order_by('fechaPubli').reverse()

	editorial2 = Editorial.objects.get(pk=2)
	librosEd2 = editorial2.libro_set.all()
	librosEd2 = librosEd2.order_by('fechaPubli').reverse()

	
	context = {'libro1': librosEd1[0], 'libro2': librosEd2[0]}
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