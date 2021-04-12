from django.db import models

# Create your models here.


class ContactModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=500)
    message = models.CharField(max_length=500)