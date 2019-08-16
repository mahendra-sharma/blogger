from rest_framework import serializers
from ..models.user import UserModel


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = '__all__'
