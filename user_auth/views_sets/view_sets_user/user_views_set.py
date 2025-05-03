from platform import freedesktop_os_release

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models import User
from user_auth.permissions.main_model_permission.Main_model import *
from user_auth.serializers.user_serializer.user_serializer import UserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        # Код для смены пароля
        return Response({"status": "password updated"})
