# from rest_framework import permissions
#
# class IsOwnerOrReadOnlyHomework(permissions.BasePermission):
#     def has_permission(self, request, view):
#         return bool(request.user and request.user.is_authenticated and request.user.role == 'student')
#
#     def has_object_permission(self, request, view, obj):
#         if request.method in permissions.SAFE_METHODS:
#             return True  # разрешаем GET, HEAD, OPTIONS всем авторизованным студентам
#         return obj.student == request.user  # изменения только своему домашнему заданию
