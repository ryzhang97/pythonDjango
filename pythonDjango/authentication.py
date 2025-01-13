from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed
from django.urls import resolve
from wx.models import WXUser


class CustomJWTAuthentication(JWTAuthentication):
    def authenticate(self, request):
        current_view_name = resolve(request.path_info).url_name
        if current_view_name == 'none':
            return None
        try:
            header = self.get_header(request)
            if header is None:
                return None
            raw_token = self.get_raw_token(header)
            if raw_token is None:
                return None
            validated_token = self.get_validated_token(raw_token)
            userid = validated_token['user_id']
            if isinstance(userid, str):
                wxuser = WXUser.objects.get(openid=userid)
                return wxuser, validated_token
            else:
                return self.get_user(validated_token), validated_token
        except AuthenticationFailed as e:
            raise AuthenticationFailed(detail={'msg': 'Token验证失败', 'code': '401'})
