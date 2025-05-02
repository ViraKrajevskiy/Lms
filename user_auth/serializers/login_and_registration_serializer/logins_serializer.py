# user_auth/serializers/login_and_registration_serializer/logins_serializer.py

from rest_framework import serializers
from user_auth.models.base_user_model.user import User

from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                "detail": "Пользователь с таким номером не найден"
            })

        if not user.check_password(password):
            raise serializers.ValidationError({
                "detail": "Неверный номер телефона или пароль"
            })

        if not user.is_active:
            raise serializers.ValidationError({
                "detail": "Аккаунт деактивирован"
            })

        attrs["user"] = user
        return attrs




def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    refresh.set_exp(from_time=datetime.now(), lifetime=timedelta(minutes=10))
    refresh.access_token.set_exp(from_time=datetime.now(), lifetime=timedelta(minutes=10))
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
