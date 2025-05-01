from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.pay_model_salary.pay_model_for_student import StudentPay
from user_auth.permissions.pay_model_permission.student_pay_model_permission import StudentPayPermissions
from user_auth.permissions.special_permissions.special_permissions import IsSupervisor, IsStudent, IsStaff, IsAdmin, \
    IsTeacher
from user_auth.serializers.pay_serializer.pay_student_serializer import PayStudentSerializer


class PayStudentViewsSet(viewsets.ModelViewSet):
    queryset = StudentPay.objects.all()
    serializer_class = PayStudentSerializer
    permission_classes = [IsAuthenticated, StudentPayPermissions]