from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_active')
    # list_filter = ('category', 'is_active')
    # search_fields = ('title', 'content')
    # list_editable = ('is_active',)


admin.site.register(models.Post)
admin.site.register(models.Category)
