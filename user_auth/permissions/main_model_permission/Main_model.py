from rest_framework.permissions import BasePermission, SAFE_METHODS

# Матрица прав доступа по ролям для ViewSet-ов (имя без 'ViewSet')
ROLE_PERMISSIONS = {
    'User': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],  # admin может создавать, просматривать, обновлять
        'student': ['retrieve', 'partial_update'],            # студент только свои данные и пароль смена через OTP
        'teacher': ['retrieve', 'partial_update'],            # учитель свои данные, может менять только номер
        'worker': ['retrieve', 'partial_update'],             # staff свои данные, может менять данные проживания
    },
    'GroupHomework': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': '__all__',
        'teacher': ['list', 'retrieve', 'create', 'update'],  # учитель может CRUD кроме удаления
        'student': ['list', 'retrieve'],                      # студент видит домашки своей группы
    },
    'StudentHomework': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': '__all__',
        'student': ['create', 'list', 'retrieve', 'update'],  # студент загружает/редактирует до дедлайна
    },
    'Room': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve', 'create', 'update'],   # staff может CRUD кроме удаления
    },
    'Lesson': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve', 'create', 'update'],
        'teacher': ['list', 'retrieve', 'create', 'update'],  # учитель может CRUD кроме удаления
        'student': ['list', 'retrieve'],                      # студент может просматривать и оценивать один раз
    },
    'PayStudent': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve'],                       # staff просматривать
        'student': ['create', 'list', 'retrieve'],            # студент оплачивает и смотрит свои платежи
    },
    'PayForWorker': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve'],
    },
    'Attendance': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve'],
        'teacher': ['list', 'retrieve', 'create', 'update'],  # учитель отмечает посещаемость
    },
    'StudyDay': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'CourseDuration': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'CourseLevel': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'Course': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'Group': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve', 'create', 'update'],
        'teacher': ['list', 'retrieve'],                      # учитель видит свою группу
        'student': ['retrieve'],                              # студент видит информацию о своей группе
    },
    'Student': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'Parent': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'Teacher': {
        'supervisor': '__all__',
        'admin': '__all__',
        'teacher': ['retrieve', 'partial_update'],            # учитель меняет только проживание и телефон
        'worker': ['list', 'retrieve'],                      # staff просматривает данные учителя
    },
    'Mentor': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve'],
        'teacher': ['retrieve', 'partial_update'],            # ментор как учитель
    },
    'WorkDay': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve'],
    },
    'WorkerAttendance': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve'],
        'teacher': ['list', 'retrieve'],                    # учитель видит посещаемость
    },
    'PositionLevel': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['list', 'retrieve'],
    },
    'Department': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['retrieve'],                             # staff только просмотр
    },
    'WorkerSalaryPayed': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['retrieve'],
        'teacher': ['list', 'retrieve'],                    # учитель видит историю оплат
    },
    'WorkerSalaryWaitedPay': {
        'supervisor': '__all__',
        'admin': '__all__',
        'worker': ['retrieve'],
    },
    'Staff': {
        'supervisor': '__all__',
        'admin': ['create', 'list', 'retrieve', 'update'],   # админ CRUD без удаления
        'teacher': ['list', 'retrieve'],                     # учитель видит только свои данные
        'worker': ['list', 'retrieve', 'partial_update'],    # staff меняет только своё проживание
    },
    'StudentAddHw': {
        'supervisor': '__all__',
        'admin': ['create', 'list', 'retrieve', 'update'],
        'teacher': ['list', 'retrieve'],                    # учитель оценивает, но не редактирует
        'worker': ['list', 'retrieve', 'update'],           # staff может менять комментарии
        'student': ['create', 'list', 'retrieve', 'update'],
    },
}


class RoleBasedPermission(BasePermission):
    """Универсальный permission-класс по матрице ROLE_PERMISSIONS"""

    def has_permission(self, request, view):
        role = getattr(request.user, 'role', None)
        view_name = view.__class__.__name__.replace('ViewSet', '')
        action = view.action

        if role == 'supervisor':
            return True

        perms = ROLE_PERMISSIONS.get(view_name, {})
        allowed = perms.get(role)
        if not allowed:
            return False
        if allowed == '__all__':
            return True
        if action in SAFE_METHODS and all(a in allowed for a in ['list', 'retrieve']):
            return True
        return action in allowed

    def has_object_permission(self, request, view, obj):
        role = getattr(request.user, 'role', None)
        view_name = view.__class__.__name__.replace('ViewSet', '')

        # Специфичные проверки по объектам
        if view_name == 'StudentHomework' and role == 'student':
            return obj.student.user == request.user
        if view_name == 'GroupHomework' and role == 'student':
            return obj.group.students.filter(id=request.user.id).exists()
        if view_name == 'GroupHomework' and role == 'teacher':
            return obj.group.teacher.user == request.user
        if view_name == 'Lesson' and role == 'student':
            return obj.students.filter(id=request.user.id).exists()
        if view_name in ['WorkerSalaryPayed', 'WorkerSalaryWaitedPay'] and role == 'worker':
            return True
        if view_name == 'Staff' and role == 'worker':
            return obj.user == request.user  # staff меняет только свои данные
        return True

# В ViewSet-ах указываем:
# permission_classes = [IsAuthenticated, RoleBasedPermission]
