# from rest_framework import permissions
#
# class IsOwnerAndCanEditHomework(permissions.BasePermission):
#     """
#     Разрешает студенту публиковать и изменять только своё ДЗ.
#     Удалять ДЗ студент не может.
#     """
#
#     def has_permission(self, request, view):
#         return (
#             request.user and
#             request.user.is_authenticated and
#             request.user.role == 'student'
#         )
#
#     def has_object_permission(self, request, view, obj):
#         # Только владелец
#         is_owner = obj.student == request.user
#
#         # Разрешаем только GET
#         if request.method in permissions.SAFE_METHODS:
#             return is_owner
#
#         # PATCH/PUT разрешены, если владелец
#         if request.method in ['PUT', 'PATCH']:
#             return is_owner
#
#         # DELETE запрещён
#         if request.method == 'DELETE':
#             return False
#
#         return False
