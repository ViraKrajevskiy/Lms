from rest_framework.permissions import IsAuthenticated, BasePermission

class StaffPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'admin':
            return view.action in ['create', 'list', 'retrieve', 'update']
        return request.user.role == 'supervisor'

permission_classes = [IsAuthenticated, StaffPermissions]