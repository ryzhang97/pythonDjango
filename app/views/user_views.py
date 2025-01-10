from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from utils.api import _res
from django.contrib.auth import authenticate


class LoginView(APIView):
    def post(self, request, format=None):
        username = request.data.get("username", None)
        password = request.data.get("password", None)
        openid = request.data.get("openid", None)
        user = authenticate(request, username=username, password=password, openid=openid)
        if user is None:
            data = None
        else:
            data = {'token': user.token}
        return Response(_res(data), status=status.HTTP_200_OK)


class UserDetailView(APIView):
    def post(self, request, format=None):
        data = {'name': 1}
        return Response(_res(data), status=status.HTTP_200_OK)
