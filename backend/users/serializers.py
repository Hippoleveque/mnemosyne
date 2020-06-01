#!/usr/bin/env python
# -*- coding: utf-8 -*-

from rest_framework import serializers
from users.models import User
from django.contrib.auth import get_user_model


class UserSerializer(serializers.Serializer):
    uuid = serializers.UUIDField(read_only=True)
    email = serializers.EmailField()
    password = serializers.CharField(max_length=255)
    
    def create(self,validated_data):
        return get_user_model().objects.create_user(
            **validated_data)
    
    