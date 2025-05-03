from rest_framework import serializers

# Сериализатор для запроса одноразового кода (OTP)
# Используется, когда пользователь хочет получить код на телефон
class RequestOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField()  # Номер телефона, на который будет отправлен OTP


# Сериализатор для подтверждения OTP и смены пароля
# Используется при восстановлении пароля или смене его по коду
class ConfirmOTPAndChangePasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField()  # Номер телефона пользователя
    otp_code = serializers.CharField(max_length=6)  # Введённый одноразовый код (обычно 6 цифр)
    new_password = serializers.CharField(min_length=8)  # Новый пароль (мин. 8 символов)
