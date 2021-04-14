from django.urls import path

from .views import *

urlpatterns = [
    # Save and create
    path('student_list_f/', student_read_create ),
    path('student_list_f/<int:pk>', student_read_update_delete), 


    path('student_list_c/', Student_Create_ReadView.as_view() ),
    path('student_list_c/<int:pk>', Student_Read_Update_DeleteView.as_view()), 

    path('login/', Login.as_view()),

    path('register/', RegisterView.as_view()),
]