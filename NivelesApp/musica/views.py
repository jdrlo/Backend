from django.shortcuts import render
from django.http import Http404

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Musica
from .serializer import MusicaSerializer

from rest_framework import viewsets, permissions

class MusicaViewSet(viewsets.ModelViewSet):
    queryset = Musica.objects.all().order_by('-created')
    serializer_class = MusicaSerializer 
    permission_classes = [permissions.AllowAny]


