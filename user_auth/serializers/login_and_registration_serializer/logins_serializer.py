from rest_framework import serializers
from user_auth.models.base_user_model.user import User

from datetime import datetime, timedelta
from rest_framework_simplejwt.tokens import RefreshToken

# Сериализатор для логина по номеру телефона и паролю
class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()  # Номер телефона, по которому производится вход
    password = serializers.CharField(write_only=True)  # Пароль, скрытый из выходного ответа

    def validate(self, attrs):
        phone_number = attrs.get("phone_number")
        password = attrs.get("password")

        # Проверка: существует ли пользователь с таким номером
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                "detail": "Пользователь с таким номером не найден"
            })

        # Проверка правильности пароля
        if not user.check_password(password):
            raise serializers.ValidationError({
                "detail": "Неверный номер телефона или пароль"
            })

        # Проверка, активен ли пользователь (может быть деактивирован админом)
        if not user.is_active:
            raise serializers.ValidationError({
                "detail": "Аккаунт деактивирован"
            })

        # Если всё успешно — добавляем пользователя в возвращаемые данные
        attrs["user"] = user
        return attrs


# Функция генерации JWT-токенов для пользователя
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)  # Генерация refresh токена для пользователя

    # Установка времени жизни refresh и access токенов (по 10 минут)
    refresh.set_exp(from_time=datetime.now(), lifetime=timedelta(minutes=20))
    refresh.access_token.set_exp(from_time=datetime.now(), lifetime=timedelta(minutes=20))

    # Возвращаем оба токена в виде строки
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }
