from rest_framework import viewsets

from user_auth.serializers.group_serializers.group_serializer import GroupSerializer
from user_auth.models.student_package.model_group import Group

class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    