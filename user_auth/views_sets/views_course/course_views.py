from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.course_serializer.course_and_other import *

# ViewSet для работы с курсами
# Используется для получения, создания, обновления и удаления данных курса
class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Защита: только для авторизованных пользователей с ролью

# ViewSet для работы с днями учебного процесса
# Ожидается использование для отображения и изменения информации о днях курса
class StudyDayViewSet(viewsets.ModelViewSet):
    queryset = StudyDay.objects.all()
    serializer_class = StudyDaySerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

# ViewSet для продолжительности курса
# Это ViewSet позволяет получать/менять продолжительность различных курсов
class CourseDurationViewSet(viewsets.ModelViewSet):
    queryset = CourseDuration.objects.all()
    serializer_class = CourseDurationSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

# ViewSet для уровней курса
# Обеспечивает CRUD операции для уровней курсов (например, базовый, продвинутый)
class CourseLevelViewSet(viewsets.ModelViewSet):
    queryset = CourseLevel.objects.all()
    serializer_class = CourseLevelSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]
