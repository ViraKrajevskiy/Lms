from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from user_auth.serializers.login_and_registration_serializer.logins_serializer import LoginSerializer, \
    get_tokens_for_user

class LoginApi(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        request_body=LoginSerializer,
        responses={
            200: openapi.Response(
                description="Успешный вход",
                schema=openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        'refresh': openapi.Schema(type=openapi.TYPE_STRING),
                        'access': openapi.Schema(type=openapi.TYPE_STRING),
                        'user_id': openapi.Schema(type=openapi.TYPE_INTEGER),
                        'phone_number': openapi.Schema(type=openapi.TYPE_STRING),
                        'role': openapi.Schema(type=openapi.TYPE_STRING),
                        'is_admin': openapi.Schema(type=openapi.TYPE_BOOLEAN),
                    }
                )
            ),
            400: "Неверные данные",
            401: "Неверные учетные данные"
        }
    )
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        tokens = get_tokens_for_user(user)
        return Response(tokens, status=status.HTTP_200_OK)
