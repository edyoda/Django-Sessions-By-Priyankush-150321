from student_api.models import Student
from student_api.serializers import StudentSerializers

from rest_framework import generics

class StuListView(generics.ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StuCreateView(generics.CreateAPIView):
    serializer_class = StudentSerializers

class StuUpdateView(generics.UpdateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers

class StuDeleteView(generics.DestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializers
