from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField(default=20)
    marks = models.IntegerField(default=35)
    address = models.CharField(max_length=500)

    class Meta:
        ordering = ['-id']



