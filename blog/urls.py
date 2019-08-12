from django.urls import include, path
from .views import blogview, userview

urlpatterns = [
    path('api/user/', userview.UserView.as_view()),
    path('api/blog/', blogview.BlogView.as_view())
]
