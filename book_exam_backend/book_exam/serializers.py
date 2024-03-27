from rest_framework import serializers
from .models import Notepad , ExamDetail
from account.models import User
from subject.models import Subject
from django.utils.translation import gettext_lazy as _
from account.serializers import UserSerializer
from subject.serializaers import SubjectSerializer

class NotepadSerializers(serializers.ModelSerializer):
    default_error_messages = {
        'Subject_already_exists': _('This Subject already exists.')
    }
    student = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=True)
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), required=True)
    
    studentNotepad = UserSerializer(source='student', read_only=True)
    subjectNotepad = SubjectSerializer(source='subject', read_only=True)

    class Meta:
        model = Notepad
        fields = [
            "id",
            "description",
            "subject",
            "student",
            "studentNotepad",
            "subjectNotepad"
        ]

    def validate(self, attrs):
        student = attrs.get('student')
        subject = attrs.get('subject')
        # Check if the instance is being updated (self.instance is not None) or created (self.instance is None)
        if self.instance:
            # For updates, check if the updated attributes match another object that is not the instance being updated
            if Notepad.objects.exclude(pk=self.instance.pk).filter(student=student, subject=subject).exists():
                raise serializers.ValidationError({'student': self.error_messages['Subject_already_exists']})
        else:
            # For creations, check if any object matches the attributes
            if Notepad.objects.filter(student=student, subject=subject).exists():
                raise serializers.ValidationError({'student': self.error_messages['Subject_already_exists']})

        return attrs
    
class ExamDetailSerializers(serializers.ModelSerializer):
    subject = serializers.PrimaryKeyRelatedField(queryset=Subject.objects.all(), required=True)
    
    subjectExamDetail = SubjectSerializer(source='subject', read_only=True)
    
    class Meta: 
        model = ExamDetail
        fields = [
            "id",
            "subject",
            "description",
            "startTime",
            "endTime",
            "subjectExamDetail",
            "date"
        ]
        
    def validate(self, attrs):
        subject = attrs.get('subject')
        if self.instance:
            if ExamDetail.objects.exclude(pk=self.instance.pk).filter(subject=subject).exists():
                raise serializers.ValidationError({'subject': self.error_messages['Subject_already_exists']})
        else:
            if ExamDetail.objects.filter(subject=subject).exists():
                raise serializers.ValidationError({'subject': self.error_messages['Subject_already_exists']})
            
        return attrs
        
        
        
    
