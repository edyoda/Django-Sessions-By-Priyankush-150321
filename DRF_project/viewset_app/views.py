from student_api.models import Student
from student_api.serializers import StudentSerializers

from rest_framework import viewsets
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
# Create your views here.


class StudentViewSet(viewsets.ViewSet):
   
    def list(self, request):
        queryset = Student.objects.all()
        serializer_obj = StudentSerializers(queryset, many=True)
        return Response(serializer_obj.data)
        
    def retrieve(self, request, pk):
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializers(student)
        return Response(serializer.data)
    
    def create(self, request):
        print('########################')
        serializer = StudentSerializers(data=request.POST)
        print('post request')
        if serializer.is_valid():
            print('valid')
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def update(self, request, pk):
        print('===================================')
        queryset = Student.objects.all()
        student = get_object_or_404(queryset, pk=pk)
        serializer = StudentSerializers(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def destroy(self, request, pk=None):
        obj = Student.objects.get(id=pk)
        obj.delete()
        return Response({"Success": "Student Deleted"})
