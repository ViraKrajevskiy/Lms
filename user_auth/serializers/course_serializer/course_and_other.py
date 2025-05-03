from rest_framework import serializers

from user_auth.models.Hw_model.model_lesson import Room
from user_auth.models.workers_models.model_teacher import *


# Сериализатор для модели StudyDay — представляет расписание/рабочие дни для курсов или преподавателей
class StudyDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = StudyDay
        fields = '__all__'  # Используем все поля модели


# Сериализатор для модели CourseDuration — определяет продолжительность курса (например, 1 месяц, 3 месяца)
class CourseDurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseDuration
        fields = '__all__'  # Включаем все поля


# Сериализатор для модели Course — представляет сам курс (например, «Python для начинающих»)
class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = '__all__'  # Все поля включены в сериализацию


# Сериализатор для модели Room — класс/аудитория, где проходят занятия
class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'  # Все поля из модели Room


# Сериализатор для модели CourseLevel — уровень сложности курса (например, начальный, средний, продвинутый)
class CourseLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourseLevel
        fields = '__all__'  # Все поля включены
