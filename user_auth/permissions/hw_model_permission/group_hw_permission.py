from rest_framework.permissions import IsAuthenticated, BasePermission

class GroupHomeworkPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role in ['supervisor', 'admin', 'worker']:
            return True
        if request.user.role == 'teacher':
            return view.action in ['create', 'list', 'retrieve']
        return False

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'teacher':
            return obj.group.teacher.user == request.user
        return True

permission_classes = [IsAuthenticated, GroupHomeworkPermissions]


