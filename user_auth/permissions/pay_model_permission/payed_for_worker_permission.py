from rest_framework.permissions import IsAuthenticated, BasePermission


class PyedForWorkerPermissions(BasePermission):
    def has_permission(self, request, view):
        return request.user.role in ['supervisor', 'admin']

permission_classes = [IsAuthenticated, PyedForWorkerPermissions]