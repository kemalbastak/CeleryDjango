from django.contrib import admin
from .models import Tasks

class TasksAdmin(admin.ModelAdmin):
    list_display = ('task_name', 'due_date')


admin.site.register(Tasks, TasksAdmin)
