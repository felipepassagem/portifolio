from django.shortcuts import render
from .models import Project, Me, Tec, Carousel
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import *

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
        # Autofill FK Client.
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()

class MeViewSet(viewsets.ModelViewSet):
        # Autofill FK Client.
    serializer_class = MeSerializer
    queryset = Me.objects.all()

class TecViewSet(viewsets.ModelViewSet):
        # Autofill FK Client.
    serializer_class = TecSerializer
    queryset = Tec.objects.all()

class CarouselViewSet(viewsets.ModelViewSet):
        # Autofill FK Client.
    serializer_class = CarouselSerializer
    queryset = Carousel.objects.all()
