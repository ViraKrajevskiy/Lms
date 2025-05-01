from rest_framework import serializers

from user_auth.models.student_package.model_attandace import *

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'

class BulkAttendanceUpdateSerializer(serializers.Serializer):
    updates = serializers.DictField()


