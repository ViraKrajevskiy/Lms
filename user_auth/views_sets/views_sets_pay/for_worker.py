from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from user_auth.models.pay_model_salary.pay_model_for_worker import PyedForWorker  # Импортируем модель для выплат сотрудникам
from user_auth.pagination import StandardResultsSetPagination
from user_auth.permissions.main_model_permission.Main_model import RoleBasedPermission  # Импортируем кастомные разрешения
from user_auth.serializers.pay_serializer.pay_staff_model import PayForWorkerSerializer  # Импортируем сериализатор для выплат

class PayForWorkerViewSet(viewsets.ModelViewSet):
    queryset = PyedForWorker.objects.all()  # Получаем все объекты PyedForWorker из базы данных
    serializer_class = PayForWorkerSerializer  # Указываем сериализатор, который будет преобразовывать данные
    permission_classes = [IsAuthenticated, RoleBasedPermission]  # Разрешаем доступ только авторизованным пользователям с нужными правами
    pagination_class = StandardResultsSetPagination