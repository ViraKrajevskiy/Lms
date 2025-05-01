from rest_framework.permissions import IsAuthenticated, BasePermission

from user_auth.permissions.student_package_permission.study_day_permission import StudyDayPermissions


class WorkDayPermissions(StudyDayPermissions):
    pass