from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from utils.api import _res
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken


class LoginView(APIView):
    def post(self, request, format=None):
        user = authenticate(request)
        if user is not None:
            refresh = RefreshToken.for_user(user)
            token = str(refresh.access_token)
            data = _res({'token': token})
        else:
            data = _res(None, "登录失败", 0)
        return Response(data, status=status.HTTP_200_OK)
