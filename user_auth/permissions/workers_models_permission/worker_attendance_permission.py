from rest_framework.permissions import IsAuthenticated, BasePermission


class WorkerAttendancePermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['supervisor', 'admin', 'worker']

permission_classes = [IsAuthenticated, WorkerAttendancePermissions]