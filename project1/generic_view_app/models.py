from django.db import models

# Create your models here.


class Student(models.Model):
    name = models.CharField(max_length=30)
    age =  models.IntegerField()
    marks =  models.IntegerField()
    address = models.CharField(max_length = 200)

    def __str__(self):
        return self.name