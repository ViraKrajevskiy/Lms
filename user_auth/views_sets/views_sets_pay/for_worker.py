from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.pay_model_salary.pay_model_for_worker import PyedForWorker
from user_auth.permissions.pay_model_permission.payed_for_worker_permission import PyedForWorkerPermissions
from user_auth.permissions.special_permissions.special_permissions import IsSupervisor, IsAdmin, IsStaff
from user_auth.serializers.pay_serializer.pay_staff_model import PayForWorkerSerializer


class PayForWorkerViewSet(viewsets.ModelViewSet):
    queryset = PyedForWorker.objects.all()
    serializer_class = PayForWorkerSerializer
    permission_classes = [IsAuthenticated, PyedForWorkerPermissions]