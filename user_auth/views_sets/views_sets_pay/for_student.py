from rest_framework import viewsets

from user_auth.models.pay_model_salary.pay_model_for_student import StudentPay
from user_auth.serializers.pay_serializer.pay_student_serializer import PayStudentSerializer


class PayStudentViewsSet(viewsets.ModelViewSet):
    queryset = StudentPay.objects.all()
    serializer_class = PayStudentSerializer