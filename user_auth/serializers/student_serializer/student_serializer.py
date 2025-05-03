from rest_framework import serializers
from user_auth.models.student_package.model_student import *

# Сериализатор для модели Student — выводит все поля (ФИО, группа, user и т.д.)
class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'  # Полный доступ ко всем полям. Лучше ограничить вручную, если есть чувствительные данные.

# Сериализатор для модели Parents — тоже все поля без фильтрации
class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'
