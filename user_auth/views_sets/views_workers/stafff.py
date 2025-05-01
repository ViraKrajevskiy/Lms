from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.workers_models.model_teacher import Teacher, Mentor
from user_auth.models.workers_models.model_worker import Staff
from user_auth.pagination import StandardResultsSetPagination
from user_auth.permissions.special_permissions.special_permissions import IsSupervisor, IsAdmin, IsTeacher, IsStaff
from user_auth.permissions.workers_models_permission.mentor_permission import MentorPermissions
from user_auth.permissions.workers_models_permission.stafff_permission import StaffPermissions
from user_auth.permissions.workers_models_permission.teacher_permission import TeacherPermissions
from user_auth.serializers.stafff_serializer.staff import StaffSerializer, TeacherSerializer, MentorSerializer


class StaffViewsSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    permission_classes = [IsAuthenticated, StaffPermissions]

class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [IsAuthenticated, TeacherPermissions]

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
    permission_classes = [IsAuthenticated, MentorPermissions]