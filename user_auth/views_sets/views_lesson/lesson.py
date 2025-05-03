from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.course_serializer.course_and_other import RoomSerializer
from user_auth.serializers.special_lesson_serializer.lesson_serializer import LessonSerializer, GroupHomeworkSerializer, \
StudentHomeworkSerializer,StudentAddHwSerializer

from user_auth.models.Hw_model.model_lesson import *
from user_auth.models.Hw_model.model_home_work_lesson import *
from rest_framework import viewsets


from rest_framework.permissions import IsAuthenticated

class StudentAddHwViewSet(viewsets.ModelViewSet):
    queryset = StudentAddHw.objects.all()
    serializer_class = StudentAddHwSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):

        # Студент видит только свои дополнительные файлы.

        queryset = super().get_queryset()
        if self.request.user.role == 'student':
            return queryset.filter(homework__student__user=self.request.user)  # Только добавленные файлы для домашки этого студента
        return queryset


class LessonViewsSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]


class GroupHomeworkViewSet(viewsets.ModelViewSet):
    queryset = GroupHomework.objects.all()
    serializer_class = GroupHomeworkSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

    def perform_create(self, serializer):
        # При создании домашнего задания для группы
        serializer.save()

    def get_queryset(self):

        # Переопределение метода для возврата домашнего задания для группы.
        # Студенты видят только свои домашки.

        queryset = super().get_queryset()
        if self.request.user.role == 'student':
            return queryset.filter(group__students__user=self.request.user)  # Фильтруем по группе, в которой студент состоит
        return queryset


class StudentHomeworkViewSet(viewsets.ModelViewSet):
    queryset = StudentHomework.objects.all()
    serializer_class = StudentHomeworkSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

    def perform_create(self, serializer):
        serializer.save()

    def get_queryset(self):

        # Студент видит только свои домашние задания.

        queryset = super().get_queryset()
        if self.request.user.role == 'student':
            return queryset.filter(student__user=self.request.user)  # Фильтруем только задания для этого студента
        return queryset

