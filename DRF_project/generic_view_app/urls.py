from django.urls import path

from .views import *

urlpatterns = [
    # Save and create
    path('student_list/', StuListView.as_view()),
    path('student_create/', StuCreateView.as_view()),
    path('student_update/<int:pk>/', StuUpdateView.as_view()),
    path('student_delete/<int:pk>/', StuDeleteView.as_view()),
]