from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from utils.api import _res
from django.core.serializers import serialize
from app.serializers.user import UserSerializer
from wx.models.wx_user import WXUser

from pythonDjango.authentication import CustomJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


# user详细信息
class UserDetailView(APIView):
    # authentication_classes = [CustomJWTAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        user = request.user
        data = UserSerializer(user).data
        return Response(_res(data), status=status.HTTP_200_OK)


# openid绑定到user上
class UserBindlView(APIView):
    def post(self, request, format=None):
        openid = request.data.get("openid", None)
        user = request.user
        wxuser = WXUser.objects.get(openid=openid)
        if user.userid != wxuser.userid:
            wxuser.userid = user.userid
            wxuser.save()
        data = UserSerializer(user).data
        return Response(_res(data), status=status.HTTP_200_OK)
