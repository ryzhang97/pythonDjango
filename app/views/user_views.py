from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from utils.api import _res

from pythonDjango.authentication import CustomJWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication


class UserDetailView(APIView):
    # authentication_classes = [CustomJWTAuthentication, SessionAuthentication]
    # permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        data = {'name': 1}
        return Response(_res(data), status=status.HTTP_200_OK)
