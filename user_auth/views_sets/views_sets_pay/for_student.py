from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.pay_model_salary.pay_model_for_student import StudentPay
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.pay_serializer.pay_student_serializer import PayStudentSerializer


class PayStudentViewsSet(viewsets.ModelViewSet):
    queryset = StudentPay.objects.all()
    serializer_class = PayStudentSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]