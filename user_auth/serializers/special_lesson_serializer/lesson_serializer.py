from django.utils import timezone

from rest_framework import serializers
from user_auth import models

from user_auth.models.Hw_model.model_home_work_lesson import GroupHomework, StudentAddHw, StudentHomework
from user_auth.models.Hw_model.model_lesson import Lesson


# Сериализатор для уроков — просто выводит все поля модели Lesson
class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


# Сериализатор для группового домашнего задания — без кастомной логики
class GroupHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupHomework
        fields = '__all__'


# Сериализатор для индивидуального домашнего задания
class StudentHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHomework
        fields = '__all__'
        read_only_fields = ['is_checked', 'submitted_at']  # Эти поля не должны редактироваться студентом

    def validate(self, data):
        user = self.context['request'].user
        if user.role == 'student' and data['group_homework'].deadline < timezone.now():
            raise serializers.ValidationError("Срок сдачи задания истек")
        return data


# Сериализатор для прикрепления доп. файлов/материалов к домашке
class StudentAddHwSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAddHw
        fields = '__all__'
        read_only_fields = ['uploaded_at']  # Дата загрузки устанавливается автоматически

    def validate_homework(self, value):
        # Валидация: текущий пользователь должен быть владельцем домашки
        if value.student.user != self.context['request'].user:
            raise serializers.ValidationError("Вы не автор этого домашнего задания")
        return value
