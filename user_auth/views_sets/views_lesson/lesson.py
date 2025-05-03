from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.course_serializer.course_and_other import RoomSerializer
from user_auth.serializers.special_lesson_serializer.lesson_serializer import LessonSerializer, GroupHomeworkSerializer, \
StudentHomeworkSerializer, StudentAddHwSerializer

from user_auth.models.Hw_model.model_lesson import *
from user_auth.models.Hw_model.model_home_work_lesson import *
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

# ViewSet для работы с дополнительными домашними заданиями студентов
# Студенты могут добавлять файлы для своих домашних заданий
class StudentAddHwViewSet(viewsets.ModelViewSet):
    queryset = StudentAddHw.objects.all()  # Все объекты StudentAddHw
    serializer_class = StudentAddHwSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Только авторизованные пользователи с нужной ролью

    # Переопределяем perform_create для добавления файлов
    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):
        # Если пользователь - студент, он видит только свои дополнительные файлы
        queryset = super().get_queryset()
        if self.request.user.role == 'student':
            # Фильтруем только те файлы, которые принадлежат студенту
            return queryset.filter(homework__student__user=self.request.user)
        return queryset

# ViewSet для работы с уроками
# Доступ для всех авторизованных пользователей
class LessonViewsSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()  # Все уроки
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Доступ ограничен

# ViewSet для работы с комнатами (для уроков)
# Стандартный доступ для всех авторизованных пользователей
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()  # Все комнаты
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Доступ ограничен

# ViewSet для работы с групповыми домашними заданиями
# Студенты видят только свои задания
class GroupHomeworkViewSet(viewsets.ModelViewSet):
    queryset = GroupHomework.objects.all()  # Все групповые домашки
    serializer_class = GroupHomeworkSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Доступ для авторизованных пользователей

    def perform_create(self, serializer):
        # Создание группового домашнего задания
        serializer.save()

    def get_queryset(self):
        # Студенты видят только свои домашки (по группе)
        queryset = super().get_queryset()
        if self.request.user.role == 'student':
            # Фильтруем только те домашки, которые принадлежат группе студента
            return queryset.filter(group__students__user=self.request.user)
        return queryset

# ViewSet для работы с домашними заданиями студентов
# Каждый студент может видеть только свои задания
class StudentHomeworkViewSet(viewsets.ModelViewSet):
    queryset = StudentHomework.objects.all()  # Все задания студентов
    serializer_class = StudentHomeworkSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Доступ для авторизованных пользователей

    def perform_create(self, serializer):
        # Сохраняем новое задание
        serializer.save()

    def get_queryset(self):
        # Студенты видят только свои задания
        queryset = super().get_queryset()
        if self.request.user.role == 'student':
            # Фильтруем задания только для текущего студента
            return queryset.filter(student__user=self.request.user)
        return queryset
