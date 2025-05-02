from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission
from user_auth.serializers.course_serializer.course_and_other import *

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated,RoleBasedPermission ]

class StudyDayViewSet(viewsets.ModelViewSet):
    queryset = StudyDay.objects.all()
    serializer_class = StudyDaySerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

class CourseDurationViewSet(viewsets.ModelViewSet):
    queryset = CourseDuration.objects.all()
    serializer_class = CourseDurationSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]

class CourseLevelViewSet(viewsets.ModelViewSet):
    queryset = CourseLevel.objects.all()
    serializer_class = CourseLevelSerializer
    permission_classes = [IsAuthenticated, RoleBasedPermission]
