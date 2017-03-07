# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.Serializer):

    id = serializers.ReadOnlyField()
    username = serializers.CharField()
    first_name = serializers.CharField()
    last_name = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User()
        user.first_name = validated_data.get('first_name')
        user.last_name = validated_data.get('last_name')
        user.username = validated_data.get('username')
        user.email = validated_data.get('email')
        user.set_password(validated_data.get('password'))
        user.save()
        return user

    def update(self, instance, validated_data):
        pass
