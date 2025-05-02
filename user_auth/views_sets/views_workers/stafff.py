from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.workers_models.model_teacher import Teacher, Mentor
from user_auth.models.workers_models.model_worker import Staff
from user_auth.pagination import StandardResultsSetPagination
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.stafff_serializer.staff import StaffSerializer, TeacherSerializer, MentorSerializer


class StaffViewsSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]