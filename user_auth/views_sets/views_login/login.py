from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny  # Разрешение для любых пользователей
from drf_yasg.utils import swagger_auto_schema  # Для генерации документации
from drf_yasg import openapi  # Для спецификации OpenAPI

from user_auth.serializers.login_and_registration_serializer.logins_serializer import LoginSerializer, \
    get_tokens_for_user


# View для авторизации пользователей
class LoginApi(APIView):
    # Разрешаем доступ для всех пользователей, включая неавторизованных
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=LoginSerializer,
        # Указываем, что будет использоваться сериализатор LoginSerializer для валидации данных
        responses={  # Определяем возможные ответы API
            200: openapi.Response(
                description="Успешный вход",
                schema=openapi.Schema(  # Определяем структуру ответа в случае успешного входа
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'refresh': openapi.Schema(type=openapi.TYPE_STRING),  # Токен обновления
                        'access': openapi.Schema(type=openapi.TYPE_STRING),  # Токен доступа
                        'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),  # ID пользователя
                        'phone_number': openapi.Schema(type=openapi.TYPE_STRING),  # Номер телефона
                        'role': openapi.Schema(type=openapi.TYPE_STRING),  # Роль пользователя
                        'is_admin': openapi.Schema(type=openapi.TYPE_BOOLEAN),  # Статус администратора
                    }
                )
            ),
            400: "Неверные данные",  # Ошибка в случае неверных данных
            401: "Неверные учетные данные"  # Ошибка при неверных учетных данных
        }
    )
    def post(self, request):
        """
        Обрабатывает POST-запрос для авторизации пользователя.
        Проверяет учетные данные, возвращает токены для успешной авторизации.
        """
        # Сериализация входящих данных (номер телефона и пароль)
        serializer = LoginSerializer(data=request.data)
        # Проверка валидности данных
        serializer.is_valid(raise_exception=True)

        # Получаем пользователя из сериализатора
        user = serializer.validated_data["user"]

        # Генерация токенов для пользователя (refresh и access)
        tokens = get_tokens_for_user(user)

        # Возвращаем токены и другие данные пользователя в ответе
        return Response(tokens, status=status.HTTP_200_OK)
