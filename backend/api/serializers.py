from rest_framework import serializers
from .models import Project, Me, Tec, Carousel
from django.shortcuts import get_object_or_404

class ProjectSerializer(serializers.ModelSerializer):
  class Meta:
    model = Project
    fields = [ 'id','projectName','projectDescription','projectCreatedAt','finalUser' ]

class MeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Me
    fields = ['id','name','cel','email','linkedin','instagram', 'github','birthDate', 'description', 'obs', 'img']

class TecSerializer(serializers.ModelSerializer):
  class Meta:
    model = Tec
    fields = ['id','tecName','tecLogo','tecText']

class CarouselSerializer(serializers.ModelSerializer):
  class Meta:
    model = Carousel
    fields = ['id','carTitle','carImg','carText', 'carSubText']