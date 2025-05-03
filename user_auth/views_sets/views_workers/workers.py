from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.workers_models.model_teacher import *  # Импортируем все необходимые модели, связанные с работниками
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission  # Импортируем кастомные разрешения
from user_auth.serializers.stafff_serializer.staff import *  # Импортируем сериализаторы для работы с различными моделями
from user_auth.serializers.things_for_workers_serializer.WorkerAttandanceSerializer import WorkerAttendanceSerializer  # Сериализатор для посещаемости работников
from user_auth.serializers.things_for_workers_serializer.teacher_serializer import PositionLevelSerializer, DepartmentSerializer, WorkerSalaryPayedSerializer, WorkerSalaryWaitedPaySerializer, WorkDaySerializer  # Сериализаторы для разных данных, связанных с работниками

# ViewSet для работы с уровнями должности (PositionLevel)
class PositionLevelViewSet(viewsets.ModelViewSet):
    queryset = PositionLevel.objects.all()  # Получаем все записи об уровнях должности из базы данных
    serializer_class = PositionLevelSerializer  # Указываем сериализатор для уровня должности
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Только авторизованные пользователи с нужной ролью могут использовать этот ViewSet


# ViewSet для работы с посещаемостью работников (WorkerAttendance)
class WorkerAttendanceViewSet(viewsets.ModelViewSet):
    queryset = WorkerAttendance.objects.all()  # Получаем все записи о посещаемости работников
    serializer_class = WorkerAttendanceSerializer  # Указываем сериализатор для посещаемости
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Только авторизованные пользователи с нужной ролью могут использовать этот ViewSet


# ViewSet для работы с департаментами (Department)
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()  # Получаем все записи о департаментах
    serializer_class = DepartmentSerializer  # Указываем сериализатор для департаментов
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Только авторизованные пользователи с нужной ролью могут использовать этот ViewSet


# ViewSet для работы с выплаченной зарплатой работников (WorkerSalaryPayed)
class WorkerSalaryPayedViewSet(viewsets.ModelViewSet):
    queryset = WorkerSalaryPayed.objects.all()  # Получаем все записи о выплаченной зарплате работников
    serializer_class = WorkerSalaryPayedSerializer  # Указываем сериализатор для выплаченной зарплаты
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Только авторизованные пользователи с нужной ролью могут использовать этот ViewSet


# ViewSet для работы с ожидаемой зарплатой работников (WorkerSalaryWaitedPay)
class WorkerSalaryWaitedPayViewSet(viewsets.ModelViewSet):
    queryset = WorkerSalaryWaitedPay.objects.all()  # Получаем все записи о зарплатах, которые ожидают выплаты
    serializer_class = WorkerSalaryWaitedPaySerializer  # Указываем сериализатор для ожидаемой зарплаты
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Только авторизованные пользователи с нужной ролью могут использовать этот ViewSet


# ViewSet для работы с рабочими днями работников (WorkDay)
class WorkDayViewSet(viewsets.ModelViewSet):
    queryset = WorkDay.objects.all()  # Получаем все записи о рабочих днях работников
    serializer_class = WorkDaySerializer  # Указываем сериализатор для рабочих дней
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Только авторизованные пользователи с нужной ролью могут использовать этот ViewSet
