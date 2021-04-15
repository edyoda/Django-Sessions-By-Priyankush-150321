from student_api.models import Student
from student_api.serializers import StudentSerializers
from rest_framework.response import Response

from rest_framework import generics

# import package for filter
from rest_framework import filters

class StuListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['first_name', 'last_name']

class StuCreateView(generics.CreateAPIView):
    serializer_class = StudentSerializers

class StuUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StuDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        data = self.perform_destroy(instance)
        return Response({"Success": "Student Deleted"})
