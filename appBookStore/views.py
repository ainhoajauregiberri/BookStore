from django.http import HttpResponse, Http404
from django.http.response import HttpResponseRedirect
from django.shortcuts import get_object_or_404, get_list_or_404
from django.shortcuts import render

from appBookStore.forms import UsuarioForm, UsuariosExistentesForm, ValoracionCrear
from .models import Autor, Genero, Idioma, Editorial, Libro, Usuario, Valoracion

from pprint import pprint


#devuelve el usuario que ha iniciado sesion
def inicio(request):
	form = UsuariosExistentesForm()
	context = {'form' : form}
	return render(request, 'inicio.html', context)

def iniciarSesionUsuario(request):
	usuarios = get_list_or_404(Usuario.objects.order_by('id'))
	usuarioCorrecto = False
	passwordCorrecto = False
	if request.method=='POST':
		form= UsuariosExistentesForm(request.POST)
		if form.is_valid():
			usuarioForm = form.cleaned_data['usuario']
			passwordForm = form.cleaned_data['password']
			for usuario in usuarios:
				if usuario.usuario == usuarioForm:
					usuarioCorrecto = True
					if usuario.password == passwordForm:
						passwordCorrecto = True
			if usuarioCorrecto==True:
				if passwordCorrecto == True:
					global usuarioRegistrado 
					usuarioRegistrado = usuarioForm
					return HttpResponseRedirect('../index')
				else:
					return HttpResponse('La contraseña es incorrecta. Inténtelo de nuevo.')
			else:
				return HttpResponse('El usuario es incorrecto. Inténtelo de nuevo.')
	else:
		form = UsuarioForm()
	return render(request, 'registrarse.html', {'form' : form})


#devuelve el usuario que ha iniciado sesion
def registrarse(request):
	form = UsuarioForm()
	context = {'form' : form}
	return render(request, 'registrarse.html', context)
    
def getDatosUsuario(request):
	usuarios = get_list_or_404(Usuario.objects.order_by('id'))
	existeUsuario = False
	if request.method=='POST':
		form= UsuarioForm(request.POST)
		if form.is_valid():
			nombreForm = form.cleaned_data['nombre']
			usuarioForm = form.cleaned_data['usuario']
			passwordForm = form.cleaned_data['password']
			for usuario in usuarios:
				if usuario.usuario == usuarioForm:
					existeUsuario = True
			if existeUsuario==False:
				usuarioCreado = Usuario((usuario.id)+1, nombreForm, usuarioForm, passwordForm)
				usuarioCreado.save()
				return HttpResponseRedirect('../')
			else:
				return HttpResponse('El usuario '+usuarioForm+' ya existe. Inténtelo de nuevo.')
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
	print(usuarioRegistrado)
	context = {'libro1': librosEd1[0], 'libro2': librosEd2[0], 'usuarioRegistrado': usuarioRegistrado}
	
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
	form = ValoracionCrear()
	context = {'libro' : libro, 'autores' : autores, 'form': form}
	return render(request, 'detallesLibro.html', context)


def getDatosValoracion(request, libro_id):
	libro = get_object_or_404(Libro, pk=libro_id)
	if request.method=='POST':
		form= ValoracionCrear(request.POST)
		if form.is_valid():
			puntuacionForm = form.cleaned_data['puntuacion']
			textoForm = form.cleaned_data['texto']
			mediaValoracion=((libro.numValoraciones*libro.mediaValoracion)+contador)/(libro.numValoraciones+1)
    		libro.update({"mediaValoracion": mediaValoracion}, {"numValoraciones": libro.numValoraciones+1})
			valoracionNuevo = Valoracion(usuarioRegistrado, libro, puntuacionForm, textoForm)
			valoracionNuevo.save()
			return HttpResponseRedirect('../')
	else:
		form = ValoracionCrear()
	return render(request, 'registrarse.html', {'form' : form})



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

