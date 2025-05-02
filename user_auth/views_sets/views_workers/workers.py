# views_sets.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.workers_models.model_teacher import *
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.stafff_serializer.staff import *
from user_auth.serializers.things_for_workers_serializer.WorkerAttandanceSerializer import WorkerAttendanceSerializer
from user_auth.serializers.things_for_workers_serializer.teacher_serializer import PositionLevelSerializer,DepartmentSerializer, WorkerSalaryPayedSerializer, WorkerSalaryWaitedPaySerializer, WorkDaySerializer


class PositionLevelViewSet(viewsets.ModelViewSet):
    queryset = PositionLevel.objects.all()
    serializer_class = PositionLevelSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]


class WorkerAttendanceViewSet(viewsets.ModelViewSet):
    queryset = WorkerAttendance.objects.all()
    serializer_class = WorkerAttendanceSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]


class WorkerSalaryPayedViewSet(viewsets.ModelViewSet):
    queryset = WorkerSalaryPayed.objects.all()
    serializer_class = WorkerSalaryPayedSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]


class WorkerSalaryWaitedPayViewSet(viewsets.ModelViewSet):
    queryset = WorkerSalaryWaitedPay.objects.all()
    serializer_class = WorkerSalaryWaitedPaySerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]


class WorkDayViewSet(viewsets.ModelViewSet):
    queryset = WorkDay.objects.all()
    serializer_class = WorkDaySerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]