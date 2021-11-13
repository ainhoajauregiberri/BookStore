from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404
from .models import Autor, Genero, Idioma, Editorial, Libro


#devuelve el listado de libros de cada editorial
def index(request):
	departamentos = Departamento.objects.order_by('nombre')
	output = ', '.join([d.nombre for d in departamentos])
	return HttpResponse(output)

#devuelve los detalles de un LIBRO
def detail(request, libros_id):
	libro = Libro.objects.get(pk=libro_id)
	output = ', '.join([str(libro.id), libro.nombre, libro.editorial, str([a.nombre for a in libro.autores.all()])])
	return HttpResponse(output)

#devuelve los detalles de EDITORIALES
def editoriales(request, empleado_id):
	editorial = Editorial.objects.get(pk=editorial_id)
	output = ', '.join([str(editorial.id), editorial.nombre, str([l.nombre for l in editorial.libro_set.all()])])
	return HttpResponse(output)

#devuelve los detalles de los AUTORES
def autores(request, departamento_id):
	autor = Autor.objects.get(pk=autor_id)
	output = ', '.join([str(autor.id), autor.nombre, str([l.nombre for l in autor.libro_set.all()])])
	return HttpResponse(output)

#devuelve los detalles de un empleado
def empleado(request, empleado_id):
	empleado = Empleado.objects.get(pk=empleado_id)
	output = ', '.join([str(empleado.id), empleado.nombre, str(empleado.fecha_nacimiento), str(empleado.antiguedad), str(empleado.departamento), str([h.nombre for h in empleado.habilidades.all()])])
	return HttpResponse(output)

#devuelve los detalles de una habilidad
def habilidad(request, habilidad_id):
	habilidad = Habilidad.objects.get(pk=habilidad_id)
	output = ', '.join([str(habilidad.id), habilidad.nombre, str([e.nombre for e in habilidad.empleado_set.all()])])
	return HttpResponse(output)