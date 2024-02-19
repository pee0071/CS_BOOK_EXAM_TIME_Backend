from django.shortcuts import render
from .models import Notepad
from .serializers import NotepadSerializers
from rest_framework import viewsets

class NotepadViewSet(viewsets.ModelViewSet):
    queryset = Notepad.objects.all()
    serializer_class = NotepadSerializers
    
