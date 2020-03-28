from django.contrib import admin
from .models import (
    Articulo,
    Carrito,
    ItemCarrito,
    Empresa,
    Tipo,
)

# Register your models here.
admin.site.register(Empresa)
admin.site.register(Articulo)
admin.site.register(Tipo)
admin.site.register(Carrito)
admin.site.register(ItemCarrito)