from user_auth.serializers.special_lesson_serializer.lesson_serializer import LessonSerializer, GroupHomeworkSerializer, \
    StudentHomeworkSerializer
from user_auth.models.Hw_model.model_lesson import *
from user_auth.models.Hw_model.model_home_work_lesson import *
from user_auth.permissions.student_permissions.homework_permission import *

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated
from user_auth.permissions.student_permissions.homework_permission import *
from user_auth.permissions.student_permissions.student_permissions import *


class LessonViewsSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class GroupHomeWorkViewsSet(viewsets.ModelViewSet):
    queryset = GroupHomework.objects.all()
    serializer_class = GroupHomeworkSerializer


class StudentHomeworkViewSet(viewsets.ModelViewSet):
    queryset = StudentHomework.objects.all()
    serializer_class = StudentHomeworkSerializer
    #
    # def get_permissions(self):
    #     if self.action == 'create':
    #         return [IsAuthenticatedStudent()]
    #     elif self.action in ['update', 'partial_update']:
    #         return [IsAuthenticatedStudent(), IsOwnerOrReadOnlyHomework()]
    #     elif self.action == 'destroy':
    #         return [permissions.IsAdminUser()]  # или вообще запретить на уровне view
    #     elif self.action == 'grade':
    #         return [CanCheckHomework()]
    #     return [IsAuthenticated()]
    #
    # @action(detail=True, methods=['post'], permission_classes=[CanCheckHomework])
    # def grade(self, request, pk=None):
    #     homework = self.get_object()
    #     mark = request.data.get('mark')
    #
    #     try:
    #         mark = int(mark)
    #     except (ValueError, TypeError):
    #         return Response({'error': 'Оценка должна быть числом'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     if not (0 <= mark <= 100):
    #         return Response({'error': 'Оценка должна быть от 0 до 100'}, status=status.HTTP_400_BAD_REQUEST)
    #
    #     homework.mark = mark
    #     homework.is_checked = True
    #     homework.save()
    #     return Response({'success': f'Оценка {mark} сохранена'})
