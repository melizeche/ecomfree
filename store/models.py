from django.db import models

# Create your models here.

class Tipo(models.Model):
    codigo = models.CharField(max_length=20)
    descripcion = models.CharField(max_length=50)

    def __str__(self):
        return self.descripcion


class Articulo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(null=True, blank=True)
    precio = models.FloatField(default=0)
    tipo = models.ForeignKey("Tipo", on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='imagenes', null=True)

    def __str__(self):
        return self.nombre