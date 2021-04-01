from django.urls import path
# from .views import HomeListView,StudentDetailView, StudentDeleteViews,StudentCreateViews , create_without_form
from .views import * 

urlpatterns = [
    path('student-list', Studnet_ListView.as_view() ),
    path('home-list/', HomeListView.as_view(), name='home-list'),
    path('student/<int:pk>', StudentDetailView.as_view(), name='student-detail'),
    path('<pk>/delete/', StudentDeleteViews.as_view(),name='student-delete'),
    path('create/', StudentCreateViews.as_view(), name='student-create'),
    path('create_without_form/',create_without_form , name='create_without_form'),

]
