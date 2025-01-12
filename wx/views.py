from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from decouple import config
from utils.api import _get, _res
from wx.models.wx_user import WXUser

APPID = config('APPID')
APPSECRET = config('APPSECRET')


class LoginView(APIView):
    """
    小程序登录 获取openid、unionid
    https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/user-login/code2Session.html
    """
    # 设置空数组 不进行认证authentication
    authentication_classes = []
    permission_classes = []

    def post(self, request, format=None):
        code = request.data["code"]
        url = 'https://api.weixin.qq.com/sns/jscode2session?appid=%s&secret=%s&js_code=%s&grant_type=authorization_code' % (
            APPID, APPSECRET, code)
        res = _get(url)
        openid = res.get("openid", None)
        if openid:
            unionid = res.get("unionid", None)
            WXUser.objects.create_wx_user(openid, unionid)
        return Response(_res(res), status=status.HTTP_200_OK)


class AccessTokenView(APIView):
    """
    获取接口调用凭据 获取access_token
    https://developers.weixin.qq.com/miniprogram/dev/OpenApiDoc/mp-access-token/getAccessToken.html
    """

    def get(self, request, format=None):
        url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (
            APPID, APPSECRET)
        res = _get(url)
        data = _res(res)
        return Response(data)
