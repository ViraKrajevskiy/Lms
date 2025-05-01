from rest_framework.permissions import IsAuthenticated, BasePermission


class TeacherPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'teacher':
            return view.action in ['retrieve', 'partial_update']
        return request.user.role in ['supervisor', 'admin']

permission_classes = [IsAuthenticated, TeacherPermissions]