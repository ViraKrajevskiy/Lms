from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.pay_model_salary.pay_model_for_worker import PyedForWorker
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.pay_serializer.pay_staff_model import PayForWorkerSerializer


class PayForWorkerViewSet(viewsets.ModelViewSet):
    queryset = PyedForWorker.objects.all()
    serializer_class = PayForWorkerSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]