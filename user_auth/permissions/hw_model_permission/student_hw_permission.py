from rest_framework.permissions import IsAuthenticated, BasePermission

class StudentHomeworkPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'student':
            return view.action in ['create', 'retrieve', 'update']
        return request.user.role in ['supervisor', 'admin', 'worker']

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'student':
            return obj.student.user == request.user
        return True

permission_classes = [IsAuthenticated, StudentHomeworkPermissions]