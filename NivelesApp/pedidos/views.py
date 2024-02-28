from django.shortcuts import render
from django.http import Http404

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Pedido_Mesero, Pedido_Bodega, Inventario
from .serializer import MeseroSerializer, BodegaSerializer , InventarioSerializer

from rest_framework import viewsets, permissions

class MeseroViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Mesero.objects.all().order_by('-created')
    serializer_class = MeseroSerializer 
    permission_classes = [permissions.AllowAny]
    
class BodegaViewSet(viewsets.ModelViewSet):
    queryset = Pedido_Bodega.objects.all().order_by('-created')
    serializer_class = BodegaSerializer 
    permission_classes = [permissions.AllowAny]

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all().order_by('-created')
    serializer_class = InventarioSerializer 
    permission_classes = [permissions.AllowAny]
    
    