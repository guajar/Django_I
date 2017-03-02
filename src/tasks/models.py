from django.contrib.auth.models import User
from django.db import models


class Task(models.Model):

    PENDING = "PEN"
    DONE = "DON"
    STATUSES = (
        (PENDING, "Pending"),
        (DONE, "Done")
    )

    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=3, default=PENDING, choices=STATUSES)
    time_estimated = models.IntegerField(blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # Automáticamente añada la fecha de creación
    modified_at = models.DateTimeField(auto_now=True)  # Automáticamente actualiza la fecha al guardar
    owner = models.ForeignKey(User, related_name="owned_tasks")
    assignee = models.ForeignKey(User, related_name="assigned_tasks", null=True, default=None)

    def __str__(self):   # como toString() en Java
        return self.name
