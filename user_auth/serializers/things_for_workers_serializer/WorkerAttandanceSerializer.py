from rest_framework import serializers
from user_auth.models.workers_models.model_worker import *

class WorkerAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerAttendance
        fields = '__all__'