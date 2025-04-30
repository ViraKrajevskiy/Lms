
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from user_auth.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = User.USERNAME_FIELD

    def validate(self, attrs):
        data = super().validate(attrs)
        data.update({
            'user_id': self.user.id,
            'role': self.user.role,
            'phone_number': self.user.phone_number,
        })
        return data
