from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.pagination import StandardResultsSetPagination
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
    pagination_class = StandardResultsSetPagination



    def get_queryset(self):
        user = self.request.user

        if user.is_superuser or user.is_admin():
            return Group.objects.all()
        elif user.is_teacher():
            return Group.objects.filter(teacher__staff__user=user)
        elif user.is_supervisor():
            return Group.objects.filter(mentor__staff__user=user)
        return Group.objects.none()

    @swagger_auto_schema(
        operation_summary="Список групп",
        operation_description="Учителя видят только свои группы. Менторы — только те, где они указаны. Админы и супервайзеры — все."
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
