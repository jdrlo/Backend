from django.db import models
from django.utils.translation import gettext as _
# Create your models here.



class Eventos(models.Model):

    id_Foto = models.AutoField(primary_key=True)
    imagen_Evento = models.ImageField(verbose_name=_("Foto"),null=True, blank=True, upload_to='eventos/%Y%m/')
    precio_Palco = models.IntegerField(verbose_name=_("Precio Palco"),null=True,blank=True)
    cantidad_Personas = models.IntegerField(verbose_name=_("Cantidad Personas"),default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
