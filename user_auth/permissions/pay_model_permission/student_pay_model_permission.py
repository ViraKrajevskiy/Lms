from rest_framework.permissions import IsAuthenticated, BasePermission

class StudentPayPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'student':
            return view.action in ['create', 'list', 'retrieve']
        return request.user.role in ['supervisor', 'admin']

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'student':
            return obj.student.user == request.user
        return True

permission_classes = [IsAuthenticated, StudentPayPermissions]