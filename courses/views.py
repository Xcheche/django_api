from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets # ViewSet is a base class for all viewsets
from .models import Course # Course is a model
from .serializers import CourseSerializer # CourseSerializer is a serializer


class CourseViewSet(viewsets.ModelViewSet): 
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


