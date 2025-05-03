from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.student_package.model_student import Student, Parents
from user_auth.pagination import StandardResultsSetPagination
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.student_serializer.student_serializer import StudentSerializer, ParentsSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class StudentViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

    @action(detail=False, methods=['get'], url_path='active')
    def active_students(self, request):
        students = Student.objects.filter(student_position='active')
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='finished')
    def finished_students(self, request):
        students = Student.objects.filter(student_position='end')
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='left')
    def left_students(self, request):
        students = Student.objects.filter(student_position='left')
        serializer = self.get_serializer(students, many=True)
        return Response(serializer.data)


class ParentViewSet(viewsets.ModelViewSet):
    queryset = Parents.objects.all()
    serializer_class = ParentsSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]