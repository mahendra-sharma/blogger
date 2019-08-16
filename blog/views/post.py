from rest_framework import generics
from ..models.post import PostModel
from ..serializers.post import PostListSerializer


class PostListView(generics.ListAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer

class PostCreateView(generics.CreateAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer

class PostDetailView(generics.RetrieveAPIView):
    queryset = PostModel.objects.all()
    serializer_class = PostListSerializer
    lookup_url_kwarg= "id"
