# -*- coding: utf-8 -*-
from django import forms
from tasks.models import Task


class TaskForm(forms.ModelForm):

    class Meta:
        model = Task
        fields = ["name", "description", "time_estimated", "deadline", "assignee"]
        # exclude = [] - Campos a excluir