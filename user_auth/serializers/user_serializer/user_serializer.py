from rest_framework import serializers
from user_auth.models.base_user_model.user import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)  # Обязательное поле для пароля

    class Meta:
        model = User
        fields = ['id', 'phone_number', 'email', 'role', 'is_active', 'password']
        extra_kwargs = {
            'password': {'write_only': True}  # Убедимся, что пароль не попадет в ответ
        }

    def create(self, validated_data):
        password = validated_data.pop('password')  # Получаем пароль
        user = User(**validated_data)  # Создаем пользователя
        user.set_password(password)  # Хешируем пароль
        user.save()  # Сохраняем пользователя в базе
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        # Обновляем остальные поля
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        request = self.context.get('request')

        if request and hasattr(request, 'user') and request.user.is_student():
            representation.pop('phone_number', None)

        return representation
