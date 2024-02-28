from django.db import models
from django.utils.translation import gettext as _





class SugeQuejas(models.Model):
    id_SugeQuejas = models.AutoField(primary_key=True)
    suge_Queja = models.TextField(max_length=1000)
    estado = models.CharField(verbose_name=("Estado"),choices=[('Sugerencia', 'Sugerencia'), ('Quejas', 'Quejas')])
    fecha = models.DateTimeField(verbose_name=_("Fecha Sugerencia/Queja"), auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)