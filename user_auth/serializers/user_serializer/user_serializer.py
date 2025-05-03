from rest_framework import serializers
from user_auth.models.base_user_model.user import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'email', 'role', 'is_active']  # Укажите нужные поля

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        user = self.context['request'].user

        if user.is_student():
            representation.pop('phone_number', None)
        return representation
