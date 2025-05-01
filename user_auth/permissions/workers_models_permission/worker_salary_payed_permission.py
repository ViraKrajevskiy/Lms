from rest_framework.permissions import IsAuthenticated, BasePermission

class WorkerSalaryPayedPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == 'worker':
            return view.action == 'retrieve'
        return request.user.role in ['supervisor', 'admin']

permission_classes = [IsAuthenticated, WorkerSalaryPayedPermissions]