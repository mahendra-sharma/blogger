from rest_framework import serializers
from ..models.post import PostModel

class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostModel
        fields = '__all__'
        depth=1