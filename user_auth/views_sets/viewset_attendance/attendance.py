from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from user_auth.models.student_package.model_attandace import *
from user_auth.serializers.attendance_serializer.attendance_serializer import *


class AttendanceViewSet(viewsets.ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    @action(detail=True, methods=['patch'])
    def bulk_update(self, request, pk=None):
        attendance = self.get_object()
        updates = request.data.get('updates', {})

        # Простое обновление без проверок
        attendance.students_status.update(
            {str(k): v for k, v in updates.items()}
        )
        attendance.save()

        return Response({'status': 'success'})