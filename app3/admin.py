from django.contrib import admin
from app3.models import *

# Register your models here.
admin.site.register(User)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price']
admin.site.register(Product, ProductAdmin)


admin.site.register(Order)