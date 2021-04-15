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

# import django pagination package
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from django.conf import settings

@api_view(['GET', 'POST'])
def student_read_create(request):
    if request.method == 'GET':
        
        last_name = request.GET.get('last_name')

        print('last_name  : ',last_name)

        context={}

        page = request.GET.get('page', 1)
        obj = Student.objects.all()

        # obj is currently hold all data

        if last_name:
            obj = obj.filter(last_name__icontain=last_name)

        context['current_page'] = page

        paginator = Paginator(obj, settings.ITEM_PER_PAGE)

        try:
            page_obj = paginator.page(page)
            context['last_page'] = paginator.num_pages
        except PageNotAnInteger:
            page_obj = paginator.page(1)
        except EmptyPage:
            page_obj = paginator.page(paginator.num_pages)

        serializer_obj = StudentSerializers(page_obj, many=True)

        context['data'] = serializer_obj.data
        return Response(context)
    
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


from rest_framework.pagination import PageNumberPagination
from .pagination import PaginationHandlerMixin


class BasicPagination(PageNumberPagination):
    page_size_query_param = 'limit'

class Student_Create_ReadView(APIView, PaginationHandlerMixin):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    pagination_class = BasicPagination
    serializer_class = StudentSerializers

    def get(self, request):
        obj = Student.objects.all()
        # serializer_obj = self.serializer_class(obj, many=True)
        # return Response(serializer_obj.data)

        page = self.paginate_queryset(obj)
        if page is not None:
            serializer = self.get_paginated_response(self.serializer_class(page,many=True).data)
        else:
            serializer = self.serializer_class(obj, many=True)
        return Response(serializer.data, status=200)
    
    def post(self, request):
        context = {}
        serializer_obj = self.serializer_class(data = request.data)
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