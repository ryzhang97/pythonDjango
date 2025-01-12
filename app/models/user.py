from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models


# 自定义用户管理器
class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        创建普通用户
        """
        if not email:
            raise ValueError('用户必须有一个邮箱地址')
        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        创建超级用户
        """
        user = self.create_user(email, password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


# 自定义用户模型，继承AbstractBaseUser
class User(AbstractBaseUser):
    userid = models.IntegerField(primary_key=True, unique=True)
    username = models.CharField(max_length=50, unique=True)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=20)
    employeeid = models.IntegerField()
    last_login = models.DateTimeField(6)
    # id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # first_name = models.CharField(max_length=30, blank=True)
    # last_name = models.CharField(max_length=30, blank=True)
    # is_active = models.BooleanField(default=True)
    # is_admin = models.BooleanField(default=False)
    # is_staff = models.BooleanField(default=False)
    # date_joined = models.DateTimeField(auto_now_add=True)

    # 用于唯一标识用户的字段，这里设置为username
    USERNAME_FIELD = 'username'
    # 创建超级用户时除了USERNAME_FIELD外需要额外提供的字段，这里为空
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.username

    def check_password(self, password):
        return password == self.password

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
        db_table = 'tb_user'  # 指定使用现有的表名
