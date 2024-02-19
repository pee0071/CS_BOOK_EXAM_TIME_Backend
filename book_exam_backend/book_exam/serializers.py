from rest_framework import serializers
from .models import Notepad
from account.models import User
from subject.models import Subject

class NotepadSerializers(serializers.ModelSerializer):
    student = serializers.PrimaryKeyRelatedField(
        queryset= User.objects.all(),
        required=True
    )
     
    subject = serializers.PrimaryKeyRelatedField(
        queryset= Subject.objects.all(),
        required=True
    )
    
    class Meta:
        model = Notepad
        fields = [
            "id",
            "description",
            "subject",
            "student"
        ]
