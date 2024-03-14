
from django.db import models

class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()

class PersonalDetail(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    # Add other personal details fields

class AcademicIssue(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # Add fields for academic issues

class Course(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
