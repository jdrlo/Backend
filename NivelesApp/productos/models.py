from django.db import models
from django.utils.translation import gettext as _


# Create your models here.


#******************************************************* tabla de articulos  *************************************************


class Articulos(models.Model):
    id_Articulos = models.AutoField(primary_key=True)
    nombre_Producto = models.CharField(verbose_name=_("Nombre Producto"), max_length=30)
    precio_Producto = models.IntegerField(verbose_name=_("Precio Producto"))
    costo_Producto = models.IntegerField(verbose_name=_("Costo Producto"))
    imagen_Producto = models.ImageField(verbose_name=_("Imagen Producto"), null=True, blank=True, upload_to='articulos/%Y%m/')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nombre_Producto



