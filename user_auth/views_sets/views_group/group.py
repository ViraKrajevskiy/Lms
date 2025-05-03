from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.group_serializers.group_serializer import GroupSerializer
from user_auth.models.student_package.model_group import Group


# ViewSet для работы с группами студентов
# Позволяет выполнять операции CRUD (создание, получение, обновление, удаление) для сущности Group
class GroupViewSet(viewsets.ModelViewSet):
    # Указываем сериализатор для модели Group
    serializer_class = GroupSerializer

    # Определяем, какие объекты должны быть возвращены
    queryset = Group.objects.all()

    # Настроены разрешения: доступ только для авторизованных пользователей с нужной ролью
    permission_classes = [IsAuthenticated, RoleBasedPermission]
