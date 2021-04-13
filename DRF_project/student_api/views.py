from django.shortcuts import render
from .models import Student

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializers

# Create your views here.

@api_view(['GET', 'POST'])
def student_read_create(request):
    if request.method == 'GET':
        obj = Student.objects.all()
        serializer_obj = StudentSerializers(obj, many=True)
        return Response(serializer_obj.data)
    
    if request.method == 'POST':
        context = {}
        serializer_obj = StudentSerializers(data = request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            context['message'] ='data is creataed successfully.' 
            context['data'] = serializer_obj.data
            context['status'] = 201
        else:
            context['message'] ='data is not get creataed successfully.' 
            context['errors'] = serializer_obj.errors 
        return Response(context)


@api_view(['GET', 'PUT', 'DELETE'])
def student_read_update_delete(request,pk):
    if request.method == 'GET':
        obj = Student.objects.get(id=pk)
        serializer_obj = StudentSerializers(obj)
        return Response(serializer_obj.data)
    
    if request.method == 'PUT':
        context = {}
        
        obj = Student.objects.get(id=pk)

        serializer_obj = StudentSerializers(obj, data = request.data, partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save()
            context['message'] ='data is creataed successfully.' 
            context['data'] = serializer_obj.data
            context['status'] = 201
        else:
            context['message'] ='data is not get updated successfully.' 
            context['errors'] = serializer_obj.errors 
        return Response(context)

    if request.method == 'DELETE':
        obj = Student.objects.get(id=pk)
        obj.delete()
        return Response({'message':'Deleted successfully'})



class Student_Create_ReadView(APIView):
    def get(self, request):
        obj = Student.objects.all()
        serializer_obj = StudentSerializers(obj, many=True)
        return Response(serializer_obj.data)
    
    def post(self, request):
        context = {}
        serializer_obj = StudentSerializers(data = request.data)
        if serializer_obj.is_valid():
            serializer_obj.save()
            context['message'] ='data is creataed successfully.' 
            context['data'] = serializer_obj.data
            context['status'] = 201
        else:
            context['message'] ='data is not get creataed successfully.' 
            context['errors'] = serializer_obj.errors 
        return Response(context)


class Student_Read_Update_DeleteView(APIView):
    def get(self, request, pk):
        obj = Student.objects.get(id=pk)
        serializer_obj = StudentSerializers(obj)
        return Response(serializer_obj.data)
    
    def put(self, request, pk):
        context = {}
        
        obj = Student.objects.get(id=pk)

        serializer_obj = StudentSerializers(obj, data = request.data, partial=True)
        if serializer_obj.is_valid():
            serializer_obj.save()
            context['message'] ='data is creataed successfully.' 
            context['data'] = serializer_obj.data
            context['status'] = 201
        else:
            context['message'] ='data is not get updated successfully.' 
            context['errors'] = serializer_obj.errors 
        return Response(context)
    
    def delete(self, request, pk):
        obj = Student.objects.get(id=pk)
        obj.delete()
        return Response({'message':'Deleted successfully'})