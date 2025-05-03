from rest_framework import serializers
from user_auth.models.student_package.model_group import *

# сериалайзер группы
class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__' # all field
