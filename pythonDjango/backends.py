from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model, login

User = get_user_model()


class UserBackend(ModelBackend):
    def authenticate(self, request, **kwargs):
        try:
            openid = request.data.get("openid", None)
            if openid:
                user = User.objects.get(openid=openid)
            else:
                username = request.data.get("username", None)
                password = request.data.get("password", None)
                user = User.objects.get(username=username)
            if user.check_password(password):
                # login(request, user)
                return user
        except User.DoesNotExist:
            return None
