from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from store.models import Carrito


# Create your models here.
generos = [
    ('M', 'Masculino'),
    ('F', 'Femenino'),
    ('O', 'Otro'),
]


class Direccion(models.Model):
     ciudad = models.CharField(max_length=50)
     direccion = models.CharField(max_length=200)
     codigo_postal = models.CharField(max_length=10, null=True, blank=True)
     telefono = models.CharField(max_length=20, null=True, blank=True)
     instrucciones = models.TextField(null=True, blank=True)

     def __str__(self):
         return self.direccion

     class Meta:
        verbose_name_plural = 'Direcciones'

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='usuarios', null=True, blank=True)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    genero = models.CharField(max_length=1,choices=generos, null=True, blank=True)
    direcciones = models.ManyToManyField(Direccion)

    @property
    def nombre_completo(self):
        return f'UserId {self.user.id}: {self.user.first_name} {self.user.last_name}'

    def __str__(self):
        return self.nombre_completo

    class Meta:
        verbose_name_plural = 'Perfiles'


     

@receiver(post_save, sender=Perfil)
def crear_carrito(sender, instance, created, **kwargs):
    if created:
        Carrito.objects.create(usuario=instance)

@receiver(post_save, sender=User)
def crear_perfil(sender, instance, created, **kwargs):
    if created:
        Perfil.objects.create(user=instance)
    #instance.perfil.save()
