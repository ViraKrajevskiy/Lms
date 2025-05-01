# views_sets.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.workers_models.model_teacher import *
from user_auth.permissions.special_permissions.special_permissions import IsSupervisor, IsAdmin, IsStaff
from user_auth.permissions.workers_models_permission.WorkerSalaryWaitedPayPermission import \
    WorkerSalaryWaitedPayPermissions
from user_auth.permissions.workers_models_permission.department_permission import DepartmentPermissions
from user_auth.permissions.workers_models_permission.position_level_permission import PositionLevelPermissions
from user_auth.permissions.workers_models_permission.work_day_permission import WorkDayPermissions
from user_auth.permissions.workers_models_permission.worker_attendance_permission import WorkerAttendancePermissions
from user_auth.permissions.workers_models_permission.worker_salary_payed_permission import WorkerSalaryPayedPermissions
from user_auth.serializers.stafff_serializer.staff import *
from user_auth.serializers.things_for_workers_serializer.WorkerAttandanceSerializer import WorkerAttendanceSerializer
from user_auth.serializers.things_for_workers_serializer.teacher_serializer import PositionLevelSerializer,DepartmentSerializer, WorkerSalaryPayedSerializer, WorkerSalaryWaitedPaySerializer, WorkDaySerializer


class PositionLevelViewSet(viewsets.ModelViewSet):
    queryset = PositionLevel.objects.all()
    serializer_class = PositionLevelSerializer
    permission_classes = [IsAuthenticated, PositionLevelPermissions]


class WorkerAttendanceViewSet(viewsets.ModelViewSet):
    queryset = WorkerAttendance.objects.all()
    serializer_class = WorkerAttendanceSerializer
    permission_classes = [IsAuthenticated, WorkerAttendancePermissions]

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    permission_classes = [IsAuthenticated, DepartmentPermissions]


class WorkerSalaryPayedViewSet(viewsets.ModelViewSet):
    queryset = WorkerSalaryPayed.objects.all()
    serializer_class = WorkerSalaryPayedSerializer
    permission_classes = [IsAuthenticated, WorkerSalaryPayedPermissions]


class WorkerSalaryWaitedPayViewSet(viewsets.ModelViewSet):
    queryset = WorkerSalaryWaitedPay.objects.all()
    serializer_class = WorkerSalaryWaitedPaySerializer
    permission_classes = [IsAuthenticated, WorkerSalaryWaitedPayPermissions]


class WorkDayViewSet(viewsets.ModelViewSet):
    queryset = WorkDay.objects.all()
    serializer_class = WorkDaySerializer
    permission_classes = [IsAuthenticated, WorkDayPermissions]