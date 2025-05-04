import random
from django.utils import timezone
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from drf_yasg.utils import swagger_auto_schema
from user_auth.models.Otp_model.email_model import OTPCode
from user_auth.serializers.login_and_registration_serializer.serializer_change_password import RequestOTPSerializer, ConfirmOTPAndChangePasswordSerializer

# Получаем модель пользователя
User = get_user_model()

class RequestOTPView(APIView):
    @swagger_auto_schema(request_body=RequestOTPSerializer, responses={200: "OTP sent"})
    def post(self, request):
        serializer = RequestOTPSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        phone_number = serializer.validated_data['phone_number']

        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return Response({"detail": "Пользователь не найден"}, status=404)

        code = str(random.randint(100000, 999999))
        OTPCode.objects.create(user=user, code=code)

        # Для отладки: возвращаем код вместе с номером
        return Response({
            "detail": code,
            "phone_number": phone_number,
            # Удалить в продакшене!
        }, status=200)



class ConfirmOTPAndChangePasswordView(APIView):
    # Этот view проверяет OTP и меняет пароль
    @swagger_auto_schema(
        request_body=ConfirmOTPAndChangePasswordSerializer,
        responses={200: "Пароль успешно изменен", 400: "Ошибка валидации"}
    )
    def post(self, request):
        # Проверяем и валидируем данные запроса с использованием сериализатора
        serializer = ConfirmOTPAndChangePasswordSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone_number = serializer.validated_data['phone_number']
        otp_code = serializer.validated_data['otp_code']
        new_password = serializer.validated_data['new_password']

        # Пытаемся найти пользователя по номеру телефона
        try:
            user = User.objects.get(phone_number=phone_number)
        except User.DoesNotExist:
            return Response({"detail": "Пользователь не найден"}, status=404)

        # Пытаемся найти непогашенный OTP код для пользователя
        try:
            otp = OTPCode.objects.get(user=user, code=otp_code, is_used=False)
        except OTPCode.DoesNotExist:
            return Response({"detail": "Неверный или использованный OTP"}, status=400)

        # Проверяем, не истек ли срок действия OTP
        if otp.is_expired():
            # Если истек, помечаем его как использованный и возвращаем ошибку
            otp.is_used = True
            otp.save()
            return Response({"detail": "Срок действия OTP истёк"}, status=400)

        # Меняем пароль пользователя
        user.set_password(new_password)
        user.save()

        # Помечаем OTP как использованный
        otp.is_used = True
        otp.save()

        # Ответ об успешной смене пароля
        return Response({"detail": "Пароль успешно изменен"}, status=200)
