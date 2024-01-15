from django.contrib import admin
from . import models


class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'is_done')


admin.site.register(models.Todo, TodoAdmin)
