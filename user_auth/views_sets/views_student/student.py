from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.student_package.model_student import Student, Parents
from user_auth.pagination import StandardResultsSetPagination
from user_auth.serializers.student_serializer.student_serializer import StudentSerializer, ParentsSerializer

class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, ]


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer

    def get_permissions(self):
        if self.action in ['create', 'update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsSupervisor() | IsAdmin()]
        return [IsAuthenticated(), IsStaff() | IsTeacher()]