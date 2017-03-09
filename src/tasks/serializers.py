# -*- coding: utf-8 -*-
from rest_framework import serializers

from tasks.models import Task


class TasksListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ("id", "name", "status")


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = '__all__'
