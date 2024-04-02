from django.shortcuts import render
from .models import Notepad , ExamDetail
from .serializers import NotepadSerializers ,ExamDetailSerializers
from rest_framework import status, viewsets
from rest_framework.response import Response
from rest_framework.exceptions import NotFound

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
       
class ExamDetailViewSet(viewsets.ModelViewSet):
    queryset = ExamDetail.objects.all() #ครั้งแรกถูกประกาศให้ไป get ข้อมูลทั้งหมด 
    serializer_class = ExamDetailSerializers
    
    # http://localhost:8000/api/examdetail/
    # GET /education/department/?date=2024-03-29
    def get_queryset(self):
        queryset = ExamDetail.objects.all() #ให้ get ใหม่ครั้งนึง
        # queryset = self.queryset  # Start with the default queryset
        subject = self.request.query_params.get('subject')
        date = self.request.query_params.get('date')

        if subject:
            queryset = queryset.filter(subject__id=subject)

        # if date:
        #     queryset = queryset.filter(date=date)
        
        if date:
            queryset = queryset.filter(date__icontains=date)
        print(queryset)
        return queryset
    
    # http://localhost:8000/examdetail/ id
    # def destroy(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     self.perform_destroy(instance)
    #     return Response(status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except NotFound:
            return Response({'error': 'Exam detail not found'}, status=status.HTTP_404_NOT_FOUND)
        
    
    
        
        
    

    
