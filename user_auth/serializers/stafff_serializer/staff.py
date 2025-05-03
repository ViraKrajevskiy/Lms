from rest_framework import serializers
from user_auth.models.workers_models.model_teacher import *

# Сериализатор для модели Staff — все поля отображаются и редактируются
class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'  # Выводит все поля модели (имя, должность, отдел и т.п.)

# Сериализатор для Teacher — аналогично Staff
class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'  # Включает, вероятно, user, предметы, группы и т.п.

# Сериализатор для Mentor — ничего кастомного, просто стандартный CRUD
class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
