from django.shortcuts import render

from django.shortcuts import render
from django.http import Http404

from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import SugeQuejas
from .serializers import SugeQuejaSerializer
from rest_framework import viewsets, permissions

class SugeQuejaViewSet(viewsets.ModelViewSet):
    queryset = SugeQuejas.objects.all().order_by('-created')
    serializer_class = SugeQuejaSerializer 
    permission_classes = [permissions.IsAuthenticated]
