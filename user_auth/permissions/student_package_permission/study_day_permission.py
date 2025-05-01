from rest_framework.permissions import IsAuthenticated, BasePermission

class StudyDayPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['supervisor', 'admin', 'worker']

permission_classes = [IsAuthenticated, StudyDayPermissions]