from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Blog


def index(request,*args,**kwargs):
    return render(request,'index.html')

def blogs(request):
    obj = Blog.objects.all()
    return render(request,'index.html', {'data' : obj})


def home(request):
    return render(request,'home.html')


def sale(request):
    return render(request,'sale.html')


def order(request):
    return render(request,'order.html')
