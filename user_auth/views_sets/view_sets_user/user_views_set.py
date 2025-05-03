from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response

from user_auth.models import User
from user_auth.pagination import StandardResultsSetPagination
from user_auth.permissions.main_model_permission.Main_model import *
from user_auth.serializers.user_serializer.user_serializer import UserSerializer

# ViewSet для управления пользователями
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Авторизация + кастомные права по ролям
    pagination_class = StandardResultsSetPagination

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        # Реализовать проверку текущего пароля, валидацию нового, смену и возврат результата
        return Response({"status": "password updated"})
