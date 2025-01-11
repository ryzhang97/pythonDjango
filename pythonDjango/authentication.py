from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.urls import resolve


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        current_view_name = resolve(request.path_info).url_name
        if current_view_name == 'login':
            return None
        try:
            return super().authenticate(request)
        except AuthenticationFailed as e:
            raise AuthenticationFailed(detail={'msg': 'Token验证失败', 'code': '401'})
