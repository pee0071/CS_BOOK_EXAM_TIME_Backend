from django.db import models
from account.models import User

class Subject(models.Model):
    subjectCode = models.CharField(max_length=8, unique=True)
    subjectName = models.CharField(max_length=30)
    teacher = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)

class StudentEnrolled(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
