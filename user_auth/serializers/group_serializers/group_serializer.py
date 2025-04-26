from rest_framework import serializers
from user_auth.models.Hw_model.model_home_work_lesson import *

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'
