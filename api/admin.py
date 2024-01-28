from django.contrib import admin
from . import models


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at', 'is_active')
    # list_filter = ('category', 'is_active')
    # search_fields = ('title', 'content')
    # list_editable = ('is_active',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else None

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


admin.site.register(models.Post)
admin.site.register(models.Category)
