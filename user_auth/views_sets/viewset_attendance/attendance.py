from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from user_auth.models.student_package.model_attandace import Attendance, AttendanceRecord
from user_auth.serializers.attendance_serializer.attendance_serializer import AttendanceRecordSerializer

class AttendanceRecordViewSet(viewsets.ModelViewSet):
    queryset = AttendanceRecord.objects.all()
    serializer_class = AttendanceRecordSerializer

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):

        try:
            attendance = Attendance.objects.get(id=pk)
        except Attendance.DoesNotExist:
            return Response({"error": "Attendance record not found!"}, status=404)

        students_status = request.data.get("students_status", [])

        for status_update in students_status:
            student_id = status_update.get("student_id")
            status = status_update.get("status")
            student = attendance.group.students.get(id=student_id)

            # Обновляем или создаем запись AttendanceRecord
            AttendanceRecord.objects.update_or_create(
                attendance=attendance,
                student=student,
                defaults={"status": status}
            )

        # После обновления автоматически помечаем отсутствующих студентов
        attendance.save()  # Вызываем save для автоматического обновления статусов отсутствующих

        return Response({"message": "Attendance updated successfully!"})
