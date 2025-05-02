from rest_framework import serializers

class RequestOTPSerializer(serializers.Serializer):
    phone_number = serializers.CharField()

class ConfirmOTPAndChangePasswordSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    otp_code = serializers.CharField(max_length=6)
    new_password = serializers.CharField(min_length=8)
