from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'student', StudentViewSet, basename='student')
student_list = StudentViewSet.as_view({'get': 'list'})
student_detail = StudentViewSet.as_view({'get': 'retrieve'})
student_update = StudentViewSet.as_view({'put': 'update'})
student_add = StudentViewSet.as_view({'post': 'create'})
student_delete =StudentViewSet.as_view({'delete':'destroy'})
urlpatterns = router.urls

urlpatterns = router.urls