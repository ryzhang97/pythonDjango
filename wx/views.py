import logging
import requests

from django.http import HttpResponse, HttpResponseServerError
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from decouple import config

APPID = config('APPID')
APPSECRET = config('APPSECRET')

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')


class LoginView(APIView):
    def get(self, request, format=None):
        data = {'message': 'ok!', 'code': 200, 'data': 'login'}
        return Response(data)

    def post(self, request, format=None):
        print(request.data["code"])
        data = {'message': 'ok!', 'code': 200, 'data': 'login'}
        return Response(data, status=status.HTTP_200_OK)


class AccessTokenView(APIView):
    def get(self, request, format=None):
        res = wx_mini_token()
        if res is None:
            data = {'message': 'err!', 'code': 201, 'data': None}
        else:
            data = {'message': 'ok!', 'code': 200, 'data': res}
        return Response(data)


def wx_mini_token():
    # 设置你要请求的URL
    url = 'https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid=%s&secret=%s' % (APPID, APPSECRET)
    # 发送GET请求
    response = requests.get(url)
    # 检查请求是否成功
    if response.status_code == 200:
        # 处理成功的响应
        data = response.json()  # 如果响应是JSON格式的话
        return data
    else:
        # 处理请求失败的情况
        return None
