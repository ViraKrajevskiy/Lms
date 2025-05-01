from rest_framework.permissions import IsAuthenticated, BasePermission

class AttendancePermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'teacher':
            return view.action in ['create', 'update']
        return request.user.role in ['supervisor', 'admin', 'worker']

permission_classes = [IsAuthenticated, AttendancePermissions]