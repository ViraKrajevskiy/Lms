from rest_framework import serializers
from user_auth.models.workers_models.model_teacher import *

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Staff
        fields = '__all__'


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class MentorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mentor
        fields = '__all__'
