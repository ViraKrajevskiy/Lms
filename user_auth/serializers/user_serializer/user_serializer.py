from rest_framework import serializers
from user_auth.models.base_user_model.user import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'