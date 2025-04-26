from rest_framework import serializers
from user_auth.models.student_package.model_student import *


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'


class ParentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parents
        fields = '__all__'