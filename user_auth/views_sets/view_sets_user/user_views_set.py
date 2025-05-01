from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models import User
from user_auth.permissions.base_user_permission.base_permission import UserPermissions
from user_auth.permissions.special_permissions.special_permissions import IsSupervisor, IsAdmin
from user_auth.serializers.user_serializer.user_serializer import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated, UserPermissions]  # кастомный класс