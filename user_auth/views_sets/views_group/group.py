from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.permissions.special_permissions.special_permissions import IsSupervisor, IsAdmin, IsStaff
from user_auth.permissions.student_package_permission.group_permission import GroupPermissions
from user_auth.serializers.group_serializers.group_serializer import GroupSerializer
from user_auth.models.student_package.model_group import Group


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset =  Group.objects.all()
    permission_classes = [IsAuthenticated, GroupPermissions]