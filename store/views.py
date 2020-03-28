from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Articulo, Empresa

# Create your views here.

def home(request):
    print("El print del request", request)
    print(type(request))
    print(dir(request))
    print("El metodo http es", request.method)
    print("request.user==",request.user)
    print("----------------")
    print(dir(request.user))
    print("el objeto request.user tiene el atributo/metodo is_authenticated==", request.user.is_authenticated)
    libros = Articulo.objects.all()
    empresa = Empresa.objects.first()
    contexto = {'lista':libros, 'info':empresa, 'peticion':request}
    
    return render(request, 'lista_articulos.html', contexto)

def buscar(request, termino):
    resultado = Articulo.objects.filter(nombre__icontains=termino)
    empresa = Empresa.objects.first()
    contexto = {'lista':resultado, 'info':empresa}
    return render(request, 'lista_articulos.html', contexto)

def detalle_producto(request, id_producto):
    producto = get_object_or_404(Articulo, pk=id_producto)
    empresa = Empresa.objects.first()
    contexto = {'articulo': producto, 'info':empresa}
    return render(request, 'detalle.html', contexto)

