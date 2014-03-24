from principal.models import Bebida
from principal.models import Proyecto
from django.shortcuts import render_to_response
def lista_bebidas(request):
 bebidas = Bebida.objects.all()
 return render_to_response('lista_bebidas.html',{'lista':bebidas})
def lista_proyectos(request):
 proyectos = Proyecto.objects.all()
 return render_to_response('lista_proyectos.html',{'lista':proyectos})
