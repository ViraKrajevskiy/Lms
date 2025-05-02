from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.group_serializers.group_serializer import GroupSerializer
from user_auth.models.student_package.model_group import Group


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    queryset =  Group.objects.all()
    permission_classes = [IsAuthenticated, RoleBasedPermission]