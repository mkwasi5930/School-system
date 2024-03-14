
from django.db import models

class Course(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()

class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

class Report(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
