from django.db import models
from django.utils.translation import gettext as _
from users.models import User


#********************************************************* tabla de reservas ****************************************************


class Reservas(models.Model):
    id_Reservas = models.AutoField(primary_key=True)
    #id_Cliente = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Id Cliente"))
    nombre_Reserva = models.CharField(verbose_name=_("Nombre Reserva"),null=True)
    cantidad_Personas = models.IntegerField(verbose_name=_("Cantidad Personas"),default=0)
    ubicacion_Mesa = models.CharField(verbose_name=_("Ubicacion Mesa"), choices=[("Cualquiera","Cualquiera"),("1","1"),("2","2"),("3","3"),("4","4"),("5","5"),("6","6"),("7","7"),("8","8"),("9","9"),("10","10"),("11","11")],default='Cualquiera')
    estado_Reserva = models.CharField(verbose_name=("Estado"),choices=[('Pendiente', 'Pendiente'), ('Confirmado', 'Confirmado'), ('Denegado', 'Denegado')], default='Pendiente')
    fecha = models.DateField(verbose_name=_("fecha"),null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    