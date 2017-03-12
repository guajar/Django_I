# -*- coding: utf-8 -*-
from rest_framework.filters import SearchFilter, OrderingFilter, DjangoFilterBackend
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from tasks.models import Task
from tasks.serializers import TaskSerializer, TasksListSerializer

__author__ = 'jamal'


class TaskViewSet(ModelViewSet):

    queryset = Task.objects.all()
    permission_classes = (IsAuthenticated,)
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    search_fields = ("name", "description")
    ordering_fields = ("id", "name", "owner", "assignee", "status", "created_at")
    filter_fields = ("status", "owner", "assignee", "created_at", "deadline")

    def get_serializer_class(self):
        return TasksListSerializer if self.action == "list" else TaskSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


