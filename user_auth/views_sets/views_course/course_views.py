from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.permissions.student_package_permission.course_duration_permission import CourseDurationPermissions
from user_auth.permissions.student_package_permission.course_level_permission import CourseLevelPermissions
from user_auth.permissions.student_package_permission.course_permission import CoursePermissions
from user_auth.permissions.student_package_permission.study_day_permission import StudyDayPermissions
from user_auth.serializers.course_serializer.course_and_other import *

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [IsAuthenticated, CoursePermissions]

class StudyDayViewSet(viewsets.ModelViewSet):
    queryset = StudyDay.objects.all()
    serializer_class = StudyDaySerializer
    permission_classes = [IsAuthenticated, StudyDayPermissions]

class CourseDurationViewSet(viewsets.ModelViewSet):
    queryset = CourseDuration.objects.all()
    serializer_class = CourseDurationSerializer
    permission_classes = [IsAuthenticated, CourseDurationPermissions]

class CourseLevelViewSet(viewsets.ModelViewSet):
    queryset = CourseLevel.objects.all()
    serializer_class = CourseLevelSerializer
    permission_classes = [IsAuthenticated, CourseLevelPermissions]
