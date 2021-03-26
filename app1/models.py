from django.db import models

# Create your models here.

class Category(models.Model):
	name = models.CharField(max_length=150)
	descripton = models.CharField(max_length=1500, blank=True, null=True)

class Blog(models.Model):
	title = models.CharField(max_length=150)
	content = models.CharField(max_length=500, blank=True, null=True)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)