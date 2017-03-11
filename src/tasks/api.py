# -*- coding: utf-8 -*-
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializers import TaskSerializer, TasksListSerializer

__author__ = 'jamal'


class TaskViewSet(ModelViewSet):

    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)

    def get_serializer_class(self):
        return TasksListSerializer if self.action == "list" else TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


