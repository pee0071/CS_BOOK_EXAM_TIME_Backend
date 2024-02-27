from django.shortcuts import render
from .models import Notepad
from .serializers import NotepadSerializers
from rest_framework import viewsets

class NotepadViewSet(viewsets.ModelViewSet):
    queryset = Notepad.objects.all()
    serializer_class = NotepadSerializers
    def get_queryset(self):
        queryset = super().get_queryset()
        student= self.request.query_params.get("student")
        subject = self.request.query_params.get("subject")
        if student is not None:
            queryset = queryset.filter(student__id=student)
        if subject is not None:
            queryset = queryset.filter(subject__id=subject)
        return queryset
    
