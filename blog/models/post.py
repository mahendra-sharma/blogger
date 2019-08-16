from django.db import models
from .user import UserModel


class PostModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=10)
    auther = models.ForeignKey(UserModel, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "post"
