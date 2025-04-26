from rest_framework import viewsets
from user_auth.models import User
from user_auth.serializers.user_serializer.user_serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
