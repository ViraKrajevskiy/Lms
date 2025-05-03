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
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update'],
        'teacher': ['list', 'retrieve', 'create', 'update'],  # учитель может CRUD кроме удаления
        'student': ['list', 'retrieve'],                      # студент видит домашки своей группы
    },
    'StudentHomework': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update'],
        'student': ['create', 'list', 'retrieve', 'update'],  # студент загружает/редактирует до дедлайна
    },
    'Room': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list','retrieve', 'create', 'update'],   # staff может CRUD кроме удаления
    },
    'Lesson': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update'],
        'teacher': ['list', 'retrieve', 'create', 'update'],  # учитель может CRUD кроме удаления
        'student': ['list', 'retrieve'],                      # студент может просматривать и оценивать один раз
    },
    'PayStudent': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve'],                       # staff просматривать
        'student': ['create', 'list', 'retrieve'],            # студент оплачивает и смотрит свои платежи
    },
    'PayForWorker': {
        'supervisor': ['list', 'retrieve', 'create', 'update'],
        'admin': ['list', 'retrieve'],
        'worker': ['list', 'retrieve'],
    },
    'Attendance': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve'],
        'teacher': ['list', 'retrieve', 'create', 'update'],  # учитель отмечает посещаемость
    },
    'StudyDay': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'CourseDuration': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'CourseLevel': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'Course': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update']  ,
        'teacher':['list']
    },
    'Group': {
        'supervisor': '__all__',
        'admin':['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update'],
        'teacher': ['list', 'retrieve'],                      # учитель видит свою группу
        'student': ['retrieve'],                              # студент видит информацию о своей группе
    },
    'Student': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'Parent': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve', 'create', 'update'],
    },
    'Teacher': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'teacher': ['retrieve', 'partial_update'],            # учитель меняет только проживание и телефон
        'worker': ['list', 'retrieve'],                      # staff просматривает данные учителя
    },
    'Mentor': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve'],
        'teacher': ['retrieve', 'partial_update'],            # ментор как учитель
    },
    'WorkDay': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve'],
    },
    'WorkerAttendance': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
        'worker': ['list', 'retrieve'],
        'teacher': ['list', 'retrieve'],                    # учитель видит посещаемость
    },
    'PositionLevel': {
        'supervisor': ['list', 'retrieve', 'create', 'update'],
        'admin': ['list', 'retrieve', 'create'],
        'worker': ['list', 'retrieve'],
    },
    'Department': {
        'supervisor': '__all__',
        'admin': ['list', 'retrieve', 'create', 'update'],
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
        'admin': ['list', 'retrieve', 'create', 'update'],
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
    def has_permission(self, request, view):
        role = getattr(request.user, 'role', None)
        view_name = view.__class__.__name__.replace('ViewSet', '')
        action = view.action

        # Супервайзер может делать всё, остальные не могут удалять
        if role == 'supervisor':
            return True

        # Все остальные не могут удалять данные
        if action == 'destroy':
            return False

        # Проверка на разрешённые действия для других ролей
        perms = ROLE_PERMISSIONS.get(view_name, {})
        allowed = perms.get(role)
        if not allowed:
            return False

        if allowed == '__all__':
            return True

        if action in SAFE_METHODS:
            if any(a in allowed for a in [action]):
                return True

        return action in allowed

    def has_object_permission(self, request, view, obj):
        role = getattr(request.user, 'role', None)
        view_name = view.__class__.__name__.replace('ViewSet', '')

        # Проверка на доступ к объектам
        if view_name == 'StudentHomework' and role == 'student':
            return obj.student.user == request.user  # Студент может изменять только свои задания
        if view_name == 'GroupHomework' and role == 'student':
            return obj.group.students.filter(id=request.user.id).exists()  # Студент может только свои домашки
        if view_name == 'GroupHomework' and role == 'teacher':
            return obj.group.teacher.user == request.user  # Учитель может редактировать домашку своей группы
        if view_name == 'Lesson' and role == 'student':
            return obj.students.filter(id=request.user.id).exists()  # Студент может изменять только свои занятия
        if view_name in ['WorkerSalaryPayed', 'WorkerSalaryWaitedPay'] and role == 'worker':
            return True
        if view_name == 'Staff' and role == 'worker':
            return obj.user == request.user  # staff может редактировать только свои данные
        if view_name == 'Student' and role == 'student':  # Студент не может редактировать чужие данные
            return obj.user == request.user
        return True

# В ViewSet-ах указываем:
# permission_classes = [IsAuthenticated, RoleBasedPermission]
