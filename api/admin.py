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


class OnbordingAdmin(admin.ModelAdmin):
    list_display = ('title', 'discriptions', 'image')
    # list_filter = ('category', 'is_active')
    # search_fields = ('title', 'content')
    # list_editable = ('is_active',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else None

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('username', 'is_active', 'is_staff')
    # list_filter = ('category', 'is_active')
    # search_fields = ('title', 'content')
    # list_editable = ('is_active',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else None

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Category)
admin.site.register(models.Onbording, OnbordingAdmin)
admin.site.register(models.Register, RegisterAdmin)
