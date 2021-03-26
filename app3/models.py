from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    


class Product(models.Model):
    name =  models.CharField(max_length=50)
    price = models.IntegerField(default=0)


class Order(models.Model):
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=0)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
