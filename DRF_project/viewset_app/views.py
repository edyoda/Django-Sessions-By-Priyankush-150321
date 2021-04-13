from student_api.models import Student
from student_api.serializers import StudentSerializers

from rest_framework import viewsets
from rest_framework.response import Response

class StudentViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Student.objects.all()
        serializer_obj = StudentSerializers(queryset, many=True)
        return Response(serializer_obj.data)