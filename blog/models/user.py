from django.db import models


class UserModel(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=11)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name
