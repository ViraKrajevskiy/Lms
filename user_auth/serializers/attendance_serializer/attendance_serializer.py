from rest_framework import serializers

from user_auth.models.student_package.model_attandace import *
# тандансе сериалайзер проверка
class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = '__all__'
        read_only_fields = ['group', 'date']

    def validate(self, data):
        if self.context['request'].user.role not in ['teacher', 'worker']:
            raise serializers.ValidationError("Только преподаватели и сотрудники могут изменять посещаемость")
        return data

class BulkAttendanceUpdateSerializer(serializers.Serializer):
    updates = serializers.DictField()


