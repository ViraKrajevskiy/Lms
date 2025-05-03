from rest_framework import serializers
from user_auth.models.base_user_model.user import *

# Сериализатор кастомной модели пользователя
# Предназначен для безопасного вывода и обновления информации пользователя
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'phone_number', 'email', 'role', 'is_active']  # Только нужные поля, без пароля и токенов

    def update(self, instance, validated_data):
        # Если передан новый пароль — хешируем его через set_password
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        return super().update(instance, validated_data)

    def to_representation(self, instance):
        # Кастомизация вывода: скрываем номер телефона, если пользователь — студент
        representation = super().to_representation(instance)
        user = self.context['request'].user

        if user.is_student():
            representation.pop('phone_number', None)
        return representation
