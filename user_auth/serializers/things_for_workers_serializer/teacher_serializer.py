from rest_framework import serializers
from user_auth.models.workers_models.model_teacher import *

class WorkDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDay
        fields = '__all__'


class PositionLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionLevel
        fields = '__all__'


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'


class WorkerSalaryPayedSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerSalaryPayed
        fields = '__all__'


class WorkerSalaryWaitedPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerSalaryWaitedPay
        fields = '__all__'
