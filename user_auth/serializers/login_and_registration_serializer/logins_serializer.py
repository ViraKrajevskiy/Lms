from django.contrib.auth import get_user_model
from rest_framework import serializers, views, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
import random
from django.core.mail import send_mail

class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    password = serializers.CharField(write_only=True)

class LoginView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            try:
                user = get_user_model().objects.get(phone_number=serializer.validated_data['phone_number'])
                if user.check_password(serializer.validated_data['password']):
                    refresh = RefreshToken.for_user(user)
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                        'user_role': user.role,
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'error': 'Неверный пароль'}, status=status.HTTP_401_UNAUTHORIZED)
            except get_user_model().DoesNotExist:
                return Response({'error': 'Пользователь с таким номером телефона не найден'}, 
                              status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(views.APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh')
            if refresh_token:
                token = RefreshToken(refresh_token)
                token.blacklist()
                return Response({'success': 'Успешный выход из системы'}, status=status.HTTP_200_OK)
            return Response({'error': 'Токен не предоставлен'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class OTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    
    def validate_phone_number(self, value):
        try:
            user = get_user_model().objects.get(phone_number=value)
            return value
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("Пользователь с таким номером телефона не найден")

class OTPVerificationSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp = serializers.CharField()
    new_password = serializers.CharField(write_only=True)
    
    def validate(self, data):
        # Здесь можно добавить проверку OTP кода из кэша или базы данных
        return data

class GenerateOTPView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = OTPSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            user = get_user_model().objects.get(phone_number=phone_number)
            
            # Генерация OTP кода (здесь можно использовать библиотеку pyotp)
            otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
            
            # Сохранение OTP в кэше или базе данных (для демонстрации используем словарь)
            # В реальном приложении следует использовать безопасное хранилище
            # cache.set(f"otp_{phone_number}", otp, timeout=300)  # 5 минут
            
            # Отправка OTP по SMS (здесь нужно интегрировать SMS-сервис)
            # send_sms(phone_number, f"Ваш код подтверждения: {otp}")
            
            # Если у пользователя есть email, можно отправить OTP по почте
            if user.email:
                send_mail(
                    'Код подтверждения',
                    f'Ваш код подтверждения: {otp}',
                    'guidevirgate@gmail.com',
                    [user.email],
                    fail_silently=False,
                )
            
            return Response({'success': 'Код подтверждения отправлен'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class VerifyOTPAndChangePasswordView(views.APIView):
    def post(self, request, *args, **kwargs):
        serializer = OTPVerificationSerializer(data=request.data)
        if serializer.is_valid():
            phone_number = serializer.validated_data['phone_number']
            otp = serializer.validated_data['otp']
            new_password = serializer.validated_data['new_password']
            
            # Проверка OTP (для демонстрации)
            # saved_otp = cache.get(f"otp_{phone_number}")
            # В реальном приложении проверьте OTP из вашего хранилища
            saved_otp = "123456"  # Замените на реальную проверку
            
            if otp == saved_otp:
                try:
                    user = get_user_model().objects.get(phone_number=phone_number)
                    user.set_password(new_password)
                    user.save()
                    return Response({'success': 'Пароль успешно изменен'}, status=status.HTTP_200_OK)
                except get_user_model().DoesNotExist:
                    return Response({'error': 'Пользователь не найден'}, status=status.HTTP_404_NOT_FOUND)
            else:
                return Response({'error': 'Неверный код подтверждения'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)