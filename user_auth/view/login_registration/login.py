from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
# from user_auth.serializers.login_and_registration_serializer.logins_serializer import CustomLoginSerializer

class LoginView(APIView):
    def post(self, request):
        serializer = CustomLoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Успешный вход', 'user': serializer.validated_data['user'].phone_number}, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)
