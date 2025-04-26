# views_sets.py
from rest_framework import viewsets
from user_auth.models.workers_models.model_teacher import *
from user_auth.serializers.stafff_serializer.staff import *
from user_auth.serializers.things_for_workers_serializer.teacher_serializer import PositionLevelSerializer, \
    DepartmentSerializer, WorkerSalaryPayedSerializer, WorkerSalaryWaitedPaySerializer, WorkDaySerializer


class PositionLevelViewSet(viewsets.ModelViewSet):
    queryset = PositionLevel.objects.all()
    serializer_class = PositionLevelSerializer

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer

class WorkerSalaryPayedViewSet(viewsets.ModelViewSet):
    queryset = WorkerSalaryPayed.objects.all()
    serializer_class = WorkerSalaryPayedSerializer

class WorkerSalaryWaitedPayViewSet(viewsets.ModelViewSet):
    queryset = WorkerSalaryWaitedPay.objects.all()
    serializer_class = WorkerSalaryWaitedPaySerializer

class WorkDayViewSet(viewsets.ModelViewSet):
    queryset = WorkDay.objects.all()
    serializer_class = WorkDaySerializer