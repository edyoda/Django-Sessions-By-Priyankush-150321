from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

# home is a function based view.
def home(request):
    html = "<html><body>My First Django View</body></html>"
    return HttpResponse(html)

def index(request,*args,**kwargs):
    return render(request,'index.html')