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
    imagen = models.ImageField(upload_to='imagenes', null=True) # TODO carpetas dinamicas por tipo de producto y fecha

    def __str__(self):
        return self.nombre

class Empresa(models.Model):
    nombre = models.CharField(max_length=60)
    logo = models.ImageField(upload_to='logos', null=True, blank=True)
    slogan = models.CharField(max_length=200, null=True, blank=True)
    facebook = models.URLField(null=True, blank=True)
    instagram = models.URLField(null=True, blank=True)
    color_primario = models.CharField(max_length=7, default='#000000')
    color_secundario = models.CharField(max_length=7, default='#FFFFFF')

    def __str__(self):
        return self.nombre
    