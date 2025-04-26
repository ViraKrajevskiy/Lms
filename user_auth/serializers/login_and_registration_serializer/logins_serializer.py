from rest_framework import serializers, status, views
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import get_user_model
from django_otp.plugins.otp_totp.models import TOTPDevice
from rest_framework.permissions import IsAuthenticated


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField()
    otp = serializers.CharField()

    def validate(self, data):
        try:
            user = get_user_model().objects.get(phone_number=data['phone_number'])
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError('Пользователь с таким номером не найден')

        # Проверка OTP
        device = TOTPDevice.objects.filter(user=user).first()
        if device is None or not device.verify_token(data['otp']):
            raise serializers.ValidationError('Неверный одноразовый пароль')

        # Проверка пароля
        if not user.check_password(data['password']):
            raise serializers.ValidationError('Неверный пароль')

        return data


class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = get_user_model().objects.get(phone_number=serializer.validated_data['phone_number'])
            refresh = RefreshToken.for_user(user)
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Логаут инвалидация токенов
class LogoutView(views.APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh_token')
            token = RefreshToken(refresh_token)
            token.blacklist()  # Инвалидация токена
            return Response({"detail": "Вы успешно вышли из системы."}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
