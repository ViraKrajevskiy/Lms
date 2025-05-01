from rest_framework.permissions import IsAuthenticated, BasePermission

class LessonPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'student':
            return view.action == 'retrieve'
        return request.user.role in ['supervisor', 'admin', 'teacher', 'worker']

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'student':
            return obj.students.filter(id=request.user.id).exists()
        return True

permission_classes = [IsAuthenticated, LessonPermissions]