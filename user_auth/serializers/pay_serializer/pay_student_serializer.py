from rest_framework import serializers

from user_auth.models.pay_model_salary.pay_model_for_student import StudentPay


class PayStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPay
        fields = '__all__'
