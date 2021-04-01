from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=12)
    age = models.IntegerField(default = 18)
    address = models.TextField()

class ClassRoom(models.Model):
    room_no = models.CharField(max_length=50)
    student = models.ManyToManyField(Student)