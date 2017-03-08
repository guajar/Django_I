# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response

from tasks.models import Task
from tasks.serializers import TaskSerializer

__author__ = 'jamal'


class TasksAPI(ListCreateAPIView):
    """
    Lists (GET) and creates (POST) Tasks
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
