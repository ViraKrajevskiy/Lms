from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


# View для выхода из системы (Logout) путем блокировки токена
class LogoutApi(APIView):
    # Разрешение для всех пользователей, включая неавторизованных
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=openapi.Schema(  # Определяем структуру запроса (только refresh токен)
            type=openapi.TYPE_OBJECT,
            properties={'refresh': openapi.Schema(type=openapi.TYPE_STRING)}  # Токен для выхода
        ),
        responses={  # Определяем возможные ответы API
            205: "Токен успешно заблокирован (Logout)",  # Успешный выход
            400: "Неверный или отсутствующий токен"  # Ошибка, если токен не предоставлен или он неверный
        }
    )
    def post(self, request):
        """
        Обрабатывает POST-запрос для выхода пользователя.
        Блокирует refresh токен, чтобы пользователь больше не мог использовать его для получения нового access токена.
        """
        # Получаем refresh токен из тела запроса
        refresh_token = request.data.get("refresh")

        # Если токен не предоставлен, возвращаем ошибку
        if not refresh_token:
            return Response({"detail": "Токен refresh не предоставлен"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Создаем объект токена из переданного refresh токена
            token = RefreshToken(refresh_token)
            # Блокируем токен (для предотвращения его дальнейшего использования)
            token.blacklist()
            # Возвращаем ответ с кодом 205 (Reset Content) - успешно выполнен выход
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            # Возвращаем ошибку, если не удалось заблокировать токен
            return Response({"detail": str(e)}, status=status.HTTP_400_BAD_REQUEST)
