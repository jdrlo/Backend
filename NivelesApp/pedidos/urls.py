from django.urls import path
from .views import MeseroViewSet, BodegaViewSet, InventarioViewSet

from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static

router  = routers.DefaultRouter()
router.register('Pedido_Mesero', MeseroViewSet)
router.register('Pedido_Bodega', BodegaViewSet)
router.register('Inventario', InventarioViewSet)