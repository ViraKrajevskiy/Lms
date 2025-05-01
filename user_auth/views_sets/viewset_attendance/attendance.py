from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from user_auth.permissions.student_package_permission.attandance_permission import AttendancePermissions
from user_auth.serializers.attendance_serializer.attendance_serializer import AttendanceSerializer
from user_auth.models.student_package.model_attandace import *
from user_auth.permissions.special_permissions.special_permissions import IsTeacher, IsStaff, IsSupervisor, IsAdmin
from user_auth.serializers.attendance_serializer.attendance_serializer import *


class AttendanceViewSet(viewsets.ModelViewSet):
    serializer_class = AttendanceSerializer
    queryset =Attendance.objects.all()
    permission_classes = [IsAuthenticated, AttendancePermissions]