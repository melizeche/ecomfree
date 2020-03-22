from django.shortcuts import render
from django.http import HttpResponse

from .models import Articulo

# Create your views here.

def home(request):
    libros = Articulo.objects.all()
    contexto = {'lista':libros}
    return render(request, 'new_home.html', contexto)

def buscar(request, termino):
    resultado = Articulo.objects.filter(nombre__icontains=termino)
    contexto = {'lista':resultado}
    return render(request, 'new_home.html', contexto)