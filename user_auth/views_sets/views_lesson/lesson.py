from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.course_serializer.course_and_other import RoomSerializer
from user_auth.serializers.special_lesson_serializer.lesson_serializer import LessonSerializer, GroupHomeworkSerializer, \
StudentHomeworkSerializer,StudentAddHwSerializer

from user_auth.models.Hw_model.model_lesson import *
from user_auth.models.Hw_model.model_home_work_lesson import *

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from rest_framework.permissions import IsAuthenticated

class StudentAddHwViewSet(viewsets.ModelViewSet):
    serializer_class = StudentAddHwSerializer
    queryset = StudentAddHw.objects.all()
    permission_classes = [IsAuthenticated, RoleBasedPermission]

class LessonViewsSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

class GroupHomeWorkViewsSet(viewsets.ModelViewSet):
    queryset = GroupHomework.objects.all()
    serializer_class = GroupHomeworkSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]


class StudentHomeworkViewSet(viewsets.ModelViewSet):
    serializer_class = StudentHomeworkSerializer
    queryset = StudentHomework.objects.all()
    permission_classes = [IsAuthenticated, RoleBasedPermission]
