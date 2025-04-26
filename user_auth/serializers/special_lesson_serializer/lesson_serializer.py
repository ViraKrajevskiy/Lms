from rest_framework import serializers
from user_auth.models.Hw_model.model_lesson import *
from user_auth.models.Hw_model.model_home_work_lesson import *



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
        fields = ['id', 'group_homework', 'file', 'comment']  # не включаем mark и is_checked
        read_only_fields = ['group_homework']

