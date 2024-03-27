from django.db import models
from subject.models import Subject
from account.models import User


class Event(models.Model):
    subjectCode = models.ForeignKey(
        Subject, on_delete=models.CASCADE, null=True, blank=True
    )
    date = models.CharField(max_length=100, default="")
    startTime = models.TimeField()
    endTime = models.TimeField()
    details = models.CharField(max_length=40, default="")


class Notepad(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.TextField()
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

class ExamDetail(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    description = models.TextField()
    startTime = models.TimeField()
    endTime = models.TimeField()
    date = models.DateField(blank=True, null=True)
    