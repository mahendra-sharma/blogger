from django.urls import include, path
from .views import post, user

urlpatterns = [
    path('api/user/', include([
        path('list', user.UserListView.as_view()),
        path('create', user.UserCreateView.as_view()),
        path('<int:id>', user.UserDetailView.as_view())
    ])),
    path('api/post/', include([
        path('list', post.PostListView.as_view()),
        path('create', post.PostCreateView.as_view()),
        path('<int:id>', post.PostDetailView.as_view())
    ]))
]
