from django.contrib import admin
from tasks.models import Task

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):

    list_display = ('name', 'status', 'owner', 'assignee')
    list_filter = ('status', 'owner', 'assignee')
    search_fields = ('name', 'description')
    readonly_fields = ('created_at', 'modified_at')

    fieldsets = (
        (None, {
            "fields": ("name", "description")
        }),    # La coma es para que sepa que es una tupla (Problemas con las tuplas)
        ("Owner and assignee", {
            "fields": ("owner", "assignee"),
            "description": "Please, do not overclock your partners"
        }),
        ("Meta", {
            "fields": ("status", "time_estimated", "deadline"),
            "classes": ("collapse",)
        }),
        ("Dates", {
            "fields": ("created_at", "modified_at")
        })
    )