from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import DeleteView ,CreateView
from .models import Student
from .form import CreateForm
from django.contrib import messages
from django.views import View

class Studnet_ListView(View):
    def get(self, request):
        all_stu = Student.objects.all()
        return render(request, 'student_list_view.html', {'all_stu':all_stu})

class HomeListView(ListView):
    model = Student
    template_name = 'home-list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class StudentDetailClassView(View):
    def get(self, request):
        pass

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student_details.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class StudentDeleteViews(DeleteView):
    model = Student
    success_url ="/g_v/home-list/"


class StudentCreateViews(CreateView):
    model = Student
    template_name ='create_form.html'
    form_class = CreateForm
    success_url ="/g_v/home-list/"


def create_without_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        marks = request.POST['marks']
        address = request.POST['address']
        student = Student.objects.create(name=name,age=age,marks=marks,address=address)
        messages.success(request, 'user create successful')
        return redirect('/g_v/home-list/')
    else:
        return render(request, template_name = 'create_without_form.html')