# from rest_framework import viewsets
# from app.models import User
# from app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from app.models import User
import time


# respond公共结构
def getData(data):
    return {'message': 'ok!', 'code': 200, 'data': data}


class LoginView(APIView):
    def post(self, request, format=None):
        data = {'token': int(time.time())}
        return Response(getData(data), status=status.HTTP_200_OK)


class TestView(APIView):
    def get(self, request, format=None):
        data = {'message': 'ok!', 'code': 200, 'data': 'test'}
        return Response(data)

    def post(self, request, format=None):
        data = {'message': 'ok!', 'code': 200, 'data': 'test'}
        return Response(data, status=status.HTTP_200_OK)


class CustomView(APIView):
    def get(self, request, format=None):
        data = {'message': 'ok!', 'code': 200, 'data': 'test'}
        return Response(data)

    def post(self, request, format=None):
        data = {'message': 'Hello, World!', 'code': 200, 'data': []}
        all_objects = User.objects.all()
        for obj in all_objects:
            data['data'].append(obj.openid)
            print(obj.openid)
        return Response(data, status=status.HTTP_200_OK)
