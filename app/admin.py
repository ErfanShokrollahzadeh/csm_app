from django.contrib import admin
from .models import Category, Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'created_at')

    def image_preview(self, obj):
        return obj.image.url if obj.image else None

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
