from django.contrib import admin

from .models import Pedido_Mesero, Pedido_Bodega, Inventario

admin.site.register(Pedido_Mesero)
admin.site.register(Pedido_Bodega)
admin.site.register(Inventario)