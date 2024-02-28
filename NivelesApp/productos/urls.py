from django.urls import path
from .views import ArticulosViewSet

from django.conf import settings
from rest_framework import routers
from django.conf.urls.static import static

router  = routers.DefaultRouter()
router.register('productos', ArticulosViewSet)



