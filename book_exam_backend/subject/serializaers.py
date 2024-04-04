from rest_framework import serializers
from .models import Subject , StudentEnrolled 
from account.models import User
from account.serializers import UserSerializer

class SubjectSerializer(serializers.ModelSerializer):
    teacher = serializers.PrimaryKeyRelatedField(
        queryset= User.objects.all(),
        required=True
    )
    teacherSubject = UserSerializer(
        source = 'teacher', read_only = True
    )
    class Meta:
        model = Subject
        fields = ['subjectCode', 'subjectName', 'teacher', 'id', 'teacherSubject']
        
class StudentEnrolledSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset= User.objects.all(),
        required=True
    )
    
    subject = serializers.PrimaryKeyRelatedField(
        queryset= Subject.objects.all(),
        required=True
    )
    
    studentEnrolled = UserSerializer(
        source = 'student', read_only = True
    )
    
    subjectEnrolled = SubjectSerializer(
        source = 'subject', read_only = True
    )
    class Meta:
        model = StudentEnrolled
        fields = [
            "id",
            "student",
            "subject",
            "studentEnrolled",
            "subjectEnrolled"
        ]       
        depth = 2
        
