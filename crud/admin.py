from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(ImportExportModelAdmin):
    pass
