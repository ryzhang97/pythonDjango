from django.db import models


class User(models.Model):
    openid = models.CharField(max_length=30, primary_key=True)
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tb_user'  # 指定使用现有的表名
