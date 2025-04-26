from rest_framework import viewsets

from user_auth.models.student_package.model_student import Student, Parents
from user_auth.pagination import StandardResultsSetPagination
from user_auth.serializers.student_serializer.student_serializer import StudentSerializer, ParentsSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = StandardResultsSetPagination

class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer