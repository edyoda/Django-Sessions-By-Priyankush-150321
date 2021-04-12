from django.urls import path

from .views import *

urlpatterns = [
    # Save and create
    path('student_list_f/', student_read_create ),
    path('student_list_f/<int:pk>', student_read_update_delete), 


    path('student_list_c/', Student_Create_ReadView.as_view() ),

]