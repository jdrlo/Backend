from django.db import models
from django.utils.translation import gettext as _

# Create your models here.


class Musica(models.Model):
    id_Musica = models.AutoField(primary_key=True)
    cancion = models.CharField(verbose_name=_("Titulo Cancion"), max_length=50)
    genero = models.CharField(verbose_name=("Genero Musical"), max_length=30, blank=True, null=True)
    nombre_Artista = models.CharField(verbose_name=("Nombre Artista"), max_length=30, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
