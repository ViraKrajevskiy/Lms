from django.utils import timezone

from rest_framework import serializers
from user_auth import models

from user_auth.models.Hw_model.model_home_work_lesson import GroupHomework, StudentAddHw, StudentHomework
from user_auth.models.Hw_model.model_lesson import Lesson


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'


class GroupHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupHomework
        fields = '__all__'


class StudentHomeworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentHomework
        fields = '__all__'
        read_only_fields = ['is_checked', 'submitted_at']

    def validate(self, data):
        # Проверка дедлайна
        if data['group_homework'].deadline < timezone.now():
            raise serializers.ValidationError("Срок сдачи задания истек")
        return data

class StudentAddHwSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentAddHw
        fields = '__all__'
        read_only_fields = ['uploaded_at']

    def validate_homework(self, value):
        if value.student.user != self.context['request'].user:
            raise serializers.ValidationError("Вы не автор этого домашнего задания")
        return value
