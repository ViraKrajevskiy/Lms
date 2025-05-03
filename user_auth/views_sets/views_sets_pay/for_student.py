from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.pay_model_salary.pay_model_for_student import StudentPay
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.pay_serializer.pay_student_serializer import PayStudentSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

class PayStudentViewsSet(viewsets.ModelViewSet):
    queryset = StudentPay.objects.all()
    serializer_class = PayStudentSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

    @action(detail=False, methods=['get'], url_path='my-payments')
    def my_payments(self, request):
        user = request.user
        if not hasattr(user, 'student'):
            return Response({"detail": "Вы не являетесь студентом."}, status=403)

        payments = StudentPay.objects.filter(student=user.student)
        serializer = self.get_serializer(payments, many=True)
        return Response(serializer.data)