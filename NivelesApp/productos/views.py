from django.shortcuts import render
from django.http import Http404
 
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Articulos
from .serializer import ArticulosSerializer
from rest_framework import viewsets, permissions

class ArticulosViewSet(viewsets.ModelViewSet):
    queryset = Articulos.objects.all().order_by('-created')
    serializer_class = ArticulosSerializer 
    permission_classes = [permissions.AllowAny]