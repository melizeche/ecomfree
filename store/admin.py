from django.contrib import admin
from .models import Articulo, Tipo, Empresa

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Articulo)
admin.site.register(Tipo)
