from django.urls import path
from .views import *

urlpatterns = [
    path('contact/', contact),
    path('contact_form/', contact_form, name="contact_form"),

    path('class_view_example/', HOMEView.as_view())

]