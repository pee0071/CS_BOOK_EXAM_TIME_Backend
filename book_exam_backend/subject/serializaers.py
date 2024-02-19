from rest_framework import serializers
from .models import Subject , StudentEnrolled
from account.models import User

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ['subjectCode', 'subjectName', 'teacher']
        
class StudentEnrolledSerializer(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset= User.objects.all(),
        required=True
    )
    
    subject = serializers.PrimaryKeyRelatedField(
        queryset= Subject.objects.all(),
        required=True
    )
    class Meta:
        model = StudentEnrolled
        fields = [
            "id",
            "student",
            "subject",
        ]       
        depth = 2
