from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'student', StudentViewSet, basename='student')

student_list = StudentViewSet.as_view({'get':'list'})

urlpatterns = router.urls