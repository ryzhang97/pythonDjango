from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.serializers.user import UserSerializer
from wx.serializers import WxUserSerializer
from wx.models.wx_user import WXUser
from utils.api import _res


class UserDetailView(APIView):
    """user详细信息"""

    def post(self, request, format=None):
        user = request.user
        if user.openid:
            data = WxUserSerializer(user).data
        else:
            data = UserSerializer(user).data
        return Response(_res(data), status=status.HTTP_200_OK)


class UserBindlView(APIView):
    """openid绑定到user上"""

    def post(self, request, format=None):
        openid = request.data.get("openid", None)
        user = request.user
        wxuser = WXUser.objects.get(openid=openid)
        if user.userid != wxuser.userid:
            wxuser.userid = user.userid
            wxuser.save()
        data = UserSerializer(user).data
        return Response(_res(data), status=status.HTTP_200_OK)
