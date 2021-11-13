from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, get_list_or_404



#devuelve el listado de empresas
def index(request):
	return HttpResponse("kaixo")