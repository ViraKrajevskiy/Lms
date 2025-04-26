from rest_framework import serializers
from user_auth.models.base_user_model.user import BaseModel
from user_auth.models.pay_model_salary.pay_model_for_worker import PyedForWorker

class PayForWorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PyedForWorker
        fields = '__all__'
