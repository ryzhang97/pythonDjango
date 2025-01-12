from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from pythonDjango.enum import DataAdd


class WXManager(BaseUserManager):
    """
    微信用户管理器
    """

    def create_wx_user(self, openid, unionid=None):
        """
        创建微信用户
        :param openid:小程序openid
        :param unionid:
        :return:0:新增，1：已存在，2：更新
        """
        if not openid:
            return DataAdd.NONE
        if self.model.objects.filter(openid=openid).exists():
            if unionid:
                wx_user = self.model.objects.get(openid=openid)
                wx_user.unionid = unionid
                wx_user.save(using=self._db)
                return DataAdd.UPDATE
            return DataAdd.EXISTS
        else:
            wx_user = self.model(openid=openid, unionid=unionid)
            wx_user.save(using=self._db)
            return DataAdd.ADD


class WXUser(models.Model):
    """
    微信用户模型，继承models.Model
    """
    openid = models.CharField(primary_key=True, max_length=50, unique=True)
    unionid = models.CharField(max_length=50, unique=True)
    userid = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    # 用于唯一标识用户的字段，这里设置为username
    USERNAME_FIELD = 'openid'
    # 创建超级用户时除了USERNAME_FIELD外需要额外提供的字段，这里为空
    REQUIRED_FIELDS = []

    objects = WXManager()

    def __str__(self):
        return self.openid

    def has_perm(self, perm, obj=None):
        """
        判断用户是否有指定权限，简单返回True或False，可根据实际需求细化逻辑
        """
        return True

    def has_module_perms(self, app_label):
        """
        判断用户是否对给定的应用有访问权限，简单返回True或False，可根据实际需求细化逻辑
        """
        return True

    class Meta:
        db_table = 'tb_wx_user'
