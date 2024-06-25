from rest_framework import viewsets
from app.models import User
from app.serializers import UserSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class CustomView(APIView):
    def get(self, request, format=None):
        data = {'message': 'Hello, World!'}
        return Response(data)

    def post(self, request, format=None):
        data = {'message': 'Hello, World!'}
        return Response(data,status=status.HTTP_200_OK)
    # def post(self, request, format=None):
    #     """
    #     A simple POST example view.
    #     """
    #     serializer = MySerializer(data=request.data)
    #     if serializer.is_valid():
    #         # 处理数据，比如保存到数据库等
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
