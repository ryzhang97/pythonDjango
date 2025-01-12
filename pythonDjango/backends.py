from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model, login
from wx.models.wx_user import WXUser
import datetime

User = get_user_model()


class UserBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        try:
            openid = request.data.get("openid", None)
            if openid:
                wxuser = WXUser.objects.get(openid=openid)
                if wxuser:
                    if wxuser.userid:
                        user = User.objects.get(userid=wxuser.userid)
                        # login(request, user)
                        return user
                    else:
                        user = User()
                        user.userid = -1
                        user.username = openid
                        return user
            else:
                username = request.data.get("username", None)
                password = request.data.get("password", None)
                user = User.objects.get(username=username)
                if user.check_password(password):
                    user.last_login = datetime.datetime.now()
                    user.save()
                    # login(request, user)
                    return user
        except User.DoesNotExist:
            return None
