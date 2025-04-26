from rest_framework import serializers

from user_auth.models.Hw_model.model_lesson import Room
from user_auth.models.workers_models.model_teacher import *


class StudyDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDay
        fields = '__all__'


class CourseDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDuration
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'
