from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    previous_qualifications = models.TextField()
    academic_issues = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

