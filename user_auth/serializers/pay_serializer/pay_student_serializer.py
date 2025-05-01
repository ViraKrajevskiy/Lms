from rest_framework import serializers

from user_auth.models.pay_model_salary.pay_model_for_student import StudentPay


class PayStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentPay
        fields = '__all__'
        read_only_fields = ['payment_date']

    def validate(self, data):
        if data['payment_type'] == 'Cr' and not data.get('card_number'):
            raise serializers.ValidationError("Номер карты обязателен для оплаты картой")
        return data