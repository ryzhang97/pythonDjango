from rest_framework import serializers, views, status
from wx.models import WXUser


class WxUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = WXUser
        fields = ['openid']
