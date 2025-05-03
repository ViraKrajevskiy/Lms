from rest_framework import serializers
from user_auth.models.workers_models.model_teacher import *

# Сериализатор для модели рабочих дней (возможно — посещаемость или график)
class WorkDaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkDay
        fields = '__all__'  # Вывод всех полей: день, работник, статус и т.д.

# Уровень должности — может использоваться для сортировки зарплат или прав доступа
class PositionLevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = PositionLevel
        fields = '__all__'

# Сериализатор департамента — например, IT, HR и т.п.
class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

# Выплаченные зарплаты — вероятно, с датой и суммой
class WorkerSalaryPayedSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerSalaryPayed
        fields = '__all__'

# Ожидаемые (не выплаченные) зарплаты — оставлены только нужные поля
class WorkerSalaryWaitedPaySerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerSalaryWaitedPay
        fields = ['total_amount', 'didnt_payed_days']  # Только сумма и кол-во дней без оплаты
