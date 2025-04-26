from rest_framework import viewsets

from user_auth.models.workers_models.model_teacher import Teacher, Mentor
from user_auth.models.workers_models.model_worker import Staff
from user_auth.pagination import StandardResultsSetPagination
from user_auth.serializers.stafff_serializer.staff import StaffSerializer, TeacherSerializer, MentorSerializer


class StaffViewsSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    pagination_class = StandardResultsSetPagination

class MentorViewSet(viewsets.ModelViewSet):
    queryset = Mentor.objects.all()
    serializer_class = MentorSerializer
