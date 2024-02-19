from django.shortcuts import render
from rest_framework import viewsets
from .models import Subject , StudentEnrolled
from .serializaers import SubjectSerializer , StudentEnrolledSerializer
# Create your views here.
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    
class StudentEnrolledViewSet(viewsets.ModelViewSet):
    queryset = StudentEnrolled.objects.all()
    serializer_class = StudentEnrolledSerializer
