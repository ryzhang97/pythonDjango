from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model, login
from rest_framework_jwt.settings import api_settings

jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


class UserBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, openid=None, **kwargs):
        try:
            if openid:
                user = User.objects.get(openid=openid)
            else:
                user = User.objects.get(username=username)
                user.backend = 'app.backends.UserBackend'
            if user.check_password(password):
                # login(request, user)
                payload = jwt_payload_handler(user)
                user.token = jwt_encode_handler(payload)
                return user
        except User.DoesNotExist:
            return None
