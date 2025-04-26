# # users/serializers.py
#
# from rest_framework import serializers
# from user_auth.models.base_user_model.user import User
#
# class RegisterSerializer(serializers.ModelSerializer):
#     password = serializers.CharField(write_only=True)
#
#     class Meta:
#         model = User
#         fields = ('phone_number', 'password', )
#
#     def create(self, validated_data):
#         return User.objects.create_user(**validated_data)
