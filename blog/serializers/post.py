from rest_framework.serializers import ModelSerializer
from ..models.post import PostModel


class PostListSerializer(ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'
