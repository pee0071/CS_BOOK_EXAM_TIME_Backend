from rest_framework import serializers
from .models import Notepad
from account.models import User
from subject.models import Subject
from django.utils.translation import gettext_lazy as _

class NotepadSerializers(serializers.ModelSerializer):
    default_error_messages = {
        'Subject_already_exists': _(
            'This Subject already exists.'
        )
    }
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
    def validate(self, attrs):
        if Notepad.objects.filter(
                student=attrs.get('student')).filter(
                subject=attrs.get(
                    'subject')).exists():
            raise serializers.ValidationError({
                'student': self.error_messages['Subject_already_exists']
            })

        return attrs

    def save(self):
        data = self._validated_data
        notepad = self.Meta.model(**data)
        notepad.save()

        return NotepadSerializers(notepad).data
