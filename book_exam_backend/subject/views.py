from django.shortcuts import render
from rest_framework import viewsets
from .models import Subject , StudentEnrolled
from .serializaers import SubjectSerializer , StudentEnrolledSerializer
# Create your views here.
class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        studentCode = self.request.query_params.get("subjectCode")
        subjectName = self.request.query_params.get("subjectName")
        teacher = self.request.query_params.get("teacher")
        if teacher is not None:
            queryset = queryset.filter(teacher__id=teacher)
        if studentCode:
            queryset = queryset.filter(studentCode__icontains=studentCode)
        if subjectName: 
            queryset = queryset.filter(subjectName__icontains=subjectName)       
        return queryset
    
class StudentEnrolledViewSet(viewsets.ModelViewSet):
    queryset = StudentEnrolled.objects.all()
    serializer_class = StudentEnrolledSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        student= self.request.query_params.get("student")
        subject = self.request.query_params.get("subject")
        if student is not None:
            queryset = queryset.filter(student__id=student)
        if subject is not None:
            queryset = queryset.filter(subject__id=subject)
        return queryset
    
# class TeacherEnrolledViewSet(viewsets.ModelViewSet):
#     queryset = TeacherEnrolled.objects.all()
#     serializer_class = TeacherEnrolledSerializer
#     def get_queryset(self):
#         queryset = super().get_queryset()
#         teacher = self.request.query_params.get("teacher")
#         subject = self.request.query_params.get("subject")
#         if teacher is not None:
#             queryset = queryset.filter(teacher__id=teacher)
#         if teacher is not None:
#             queryset = queryset.filter(teacher__id=teacher)
#         return queryset
    
