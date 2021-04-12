from django.urls import path
from .views import *

urlpatterns = [
    path('test_for_cookie/', cookie_create),
    path('delete_cookie/', cookie_delete),


    path('create_session/', create_session),
    path('access_session/', access_session),
]
