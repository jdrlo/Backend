from django.db import models
from django.utils.translation import gettext as _
from users.models import User
from productos.models import Articulos

# Create your models here.

#******************************************************* tabla de pedidos de los meseros *************************************************


class Pedido_Mesero(models.Model):
    id_Orden = models.AutoField(primary_key=True)
    id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Id Usuario"),default=0)
    articulo_Id = models.ForeignKey(Articulos, on_delete=models.CASCADE, verbose_name=_("Articulos"))
    cantidad = models.IntegerField(verbose_name=_("Cantidad"))
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    '''def __str__(self):
        return self.id_Usuario'''


#******************************************************* tabla de pedidos de los meseros *************************************************


class Pedido_Bodega(models.Model):
    id_Orden_Bodega = models.AutoField(primary_key=True)
    id_Usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name=_("Id Usuario"),default=0)
    articulos_Bodega_id = models.ForeignKey(Articulos, on_delete=models.CASCADE, verbose_name=_("Articulos Pedido"))
    cantidad = models.IntegerField(verbose_name=_("Cantidad"))
    tipo_Cantidad = models.CharField(verbose_name=_("Tipo Cantidad"), choices=[("Unidad","Unidad"),("Decena","Decena"),("Docena","Docena"),("PacaX20","PacaX20"),("PacaX24","PacaX24")])
    cantidad_Total = models.IntegerField(verbose_name=_("Cantidad total"))
    estado_Pedido = models.CharField(verbose_name=("Estado"),choices=[('Pendiente', 'Pendiente'), ('Confirmado', 'Confirmado'), ('Denegado', 'Denegado')], default='Pendiente')
    fecha = models.DateTimeField(verbose_name=_("Fecha Pedido Bodega"), auto_now_add=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return f"{self.articulos_Bodega_id} - {self.fecha} - {self.cantidad_Total}"
        

    
    
class Inventario(models.Model):
    id_Inventario = models.AutoField(primary_key=True)
    id_Articulos_Inventario = models.ForeignKey(Articulos,on_delete=models.CASCADE,verbose_name=_("Articulo"))
    cantidad_Inicial = models.IntegerField(verbose_name=_("Cantididad Inicial"),default=0)
    cantidad_Final = models.IntegerField(verbose_name=_("Cantididad Final"),default=0)
    fecha = models.DateField(verbose_name=_("Fecha Inventario"), auto_now_add=True)
    pedidos_Bodega = models.IntegerField(verbose_name=_("pedido bodega"),default=0)
    cantidad_TotalVenta = models.IntegerField(verbose_name=_("Cantidad total vendido"),default=0)
    total_Venta = models.IntegerField(verbose_name=_("Venta total"),default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)