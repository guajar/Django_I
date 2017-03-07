# -*- coding: utf-8 -*-
from rest_framework.response import Response
from rest_framework.views import APIView

from tasks.models import Task
from tasks.serializers import TaskSerializer

__author__ = 'jamal'


class TasksAPI(APIView):

    def get(self, request):
        """
        Returns a list of tasks
        :param request:
        :return:
        """
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)