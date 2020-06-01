from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import Http404
from users.models import User
from rest_framework.views import APIView
from users.serializers import UserSerializer

class UserList(APIView):

    def get(self,request,format=None):
        users = User.objects.all()
        serializer = UserSerializer(users,many=True)
        return Response(serializer.data)


