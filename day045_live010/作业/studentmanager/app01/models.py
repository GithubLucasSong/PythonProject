from django.db import models

# Create your models here.

class Class(models.Model):
    name = models.CharField(max_length=32)

class Student(models.Model):
    name = models.CharField(max_length=32)
    classs = models.ForeignKey(Class,on_delete=models.CASCADE)

class Teacher(models.Model):
    name = models.CharField(max_length=32)
    subject = models.CharField(max_length=32)
    classs = models.ManyToManyField(Class)


