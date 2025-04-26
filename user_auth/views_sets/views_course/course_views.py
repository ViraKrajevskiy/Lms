from rest_framework import viewsets
from user_auth.serializers.course_serializer.course_and_other import *

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class StudyDayViewSet(viewsets.ModelViewSet):
    queryset = StudyDay.objects.all()
    serializer_class = StudyDaySerializer

class CourseDurationViewSet(viewsets.ModelViewSet):
    queryset = CourseDuration.objects.all()
    serializer_class = CourseDurationSerializer