from rest_framework import serializers
from user_auth.models.workers_models.model_worker import *

# Сериализатор посещаемости сотрудников
# Обычно включает: дату, сотрудника, статус (пришёл/опоздал/отсутствует), возможно, комментарии
class WorkerAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorkerAttendance
        fields = '__all__'  # Подходит для админки; в API лучше ограничить чувствительные поля
