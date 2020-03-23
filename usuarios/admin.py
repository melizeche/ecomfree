from django.contrib import admin
from .models import Direccion, Perfil

# Register your models here.

admin.site.register(Perfil)
admin.site.register(Direccion)