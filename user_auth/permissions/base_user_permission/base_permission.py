from rest_framework.permissions import IsAuthenticated, BasePermission


class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        if view.action == 'create':
            return request.user.is_superuser
        return True

    def has_object_permission(self, request, view, obj):
        if request.user.role == 'supervisor':
            return True
        if request.user.role == 'admin':
            return view.action in ['retrieve', 'list', 'update']
        if request.user.role == 'student':
            return obj == request.user and view.action in ['retrieve', 'partial_update']
        return False

permission_classes = [IsAuthenticated, UserPermissions]