from rest_framework.permissions import IsAuthenticated, BasePermission

class GroupPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'student':
            return view.action == 'retrieve'
        return request.user.role in ['supervisor', 'admin', 'worker']

permission_classes = [IsAuthenticated, GroupPermissions]