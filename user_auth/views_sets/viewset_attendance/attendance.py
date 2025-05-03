from rest_framework import viewsets, status  # Импортируем необходимые классы из DRF для работы с ViewSet и статусами
from rest_framework.decorators import action  # Декоратор для добавления кастомных действий в ViewSet
from rest_framework.permissions import IsAuthenticated  # Разрешение для авторизованных пользователей
from rest_framework import generics, permissions
from user_auth.pagination import StandardResultsSetPagination
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission  # Кастомное разрешение для проверки ролей
from user_auth.serializers.attendance_serializer.attendance_serializer import AttendanceSerializer  # Сериализатор для модели посещаемости
from user_auth.models.student_package.model_attandace import *  # Модели для работы с посещаемостью студентов
from user_auth.serializers.attendance_serializer.attendance_serializer import *  # Повторный импорт сериализаторов, можно оставить один

class AttendanceViewSet(viewsets.ModelViewSet):  # Создаем ViewSet для работы с моделью посещаемости
    serializer_class = AttendanceSerializer  # Указываем сериализатор для модели посещаемости
    queryset = Attendance.objects.all()  # Запрос для получения всех записей о посещаемости
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Доступ только для авторизованных пользователей с нужной ролью
    pagination_class = StandardResultsSetPagination


class MyAttendanceView(generics.ListAPIView):  # Представление только для чтения (список), показывающее посещаемость
    serializer_class = MyAttendanceSerializer  # Используем специальный сериализатор, который возвращает только нужные данные (например, без лишней информации)
    permission_classes = [permissions.IsAuthenticated]  # Доступ разрешён только авторизованным пользователям

    def get_queryset(self):  # Метод, определяющий, какие данные показывать пользователю
        user = self.request.user  # Получаем текущего авторизованного пользователя
        if not hasattr(user, 'student'):  # Если у пользователя нет связи с моделью Student, возвращаем пустой список
            return Attendance.objects.none()
        group = user.student.group  # Получаем группу, к которой относится студент
        return Attendance.objects.filter(group=group)  # Возвращаем посещаемость только для этой группы

