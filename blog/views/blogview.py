from rest_framework import generics
from ..models.blog import Blog
from ..serializers.blogserializer import BlogSerializer


class BlogView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
