from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from decouple import config
from utils.api import _get, _res

APPID = config('APPID')
APPSECRET = config('APPSECRET')


# 小程序登录
class LoginView(APIView):
    def post(self, request, format=None):
        code = request.data["code"]
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (
            APPID, APPSECRET, code)
        res = _get(url)
        data = _res(res)
        return Response(data, status=status.HTTP_200_OK)


class AccessTokenView(APIView):
    def get(self, request, format=None):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
            APPID, APPSECRET)
        res = _get(url)
        data = _res(res)
        return Response(data)
