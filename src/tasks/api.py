# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
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


class TaskDetailAPI(RetrieveUpdateDestroyAPIView):
    """
    Retrieves (GET), updates (PUT) and destroy (DELETE) a given Task
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
