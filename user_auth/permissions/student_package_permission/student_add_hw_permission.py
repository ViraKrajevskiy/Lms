from rest_framework.permissions import IsAuthenticated, BasePermission


class StudentAddHwPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'student':
            return view.action in ['create', 'retrieve', 'update']
        return request.user.role in ['supervisor', 'admin', 'teacher', 'worker']

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'student':
            return obj.homework.student.user == request.user
        return True

permission_classes = [IsAuthenticated, StudentAddHwPermissions]