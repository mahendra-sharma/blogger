from rest_framework import generics
from ..models.user import UserModel
from ..serializers.user import UserListSerializer


class UserListView(generics.ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserListSerializer


class UserCreateView(generics.CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserListSerializer


class UserDetailView(generics.RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserListSerializer
    lookup_url_kwarg = "id"
