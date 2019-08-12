from rest_framework import generics
from ..models.user import User
from ..serializers.userserializer import UserSerializer


class UserView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
