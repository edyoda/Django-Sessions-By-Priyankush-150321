# model imports
from .models import Student

# Related to view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import StudentSerializers

# related to token and login
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

# import auth and permission package
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

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
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

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


# View to manage API security
class Login(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if username is None or password is None:
            return Response({'message':'Username or password is missing.'})
        
        user_obj = authenticate(username=username, password=password)

        if not user_obj:
            return Response({'message':'Invalid credentials.'})
        
        Token.objects.filter(user=user_obj).delete()

        token, created = Token.objects.get_or_create(user=user_obj)
        return Response({'message':'Login successfully.', 'token':token.key, 'first_name':user_obj.first_name}, status=200)

from django.contrib.auth.models import User

# Handle the register logic
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        obj = User(first_name=first_name, last_name=last_name, username=username, email=username)
        obj.save()

        obj.set_password(password)

        obj.save()

        return Response({'message':'Register successfully.'}, status=200)