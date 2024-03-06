from django.contrib import admin
from .models import Post, Category, Onbording, CustomUser, SelectCountry, Topics, NewsScoure


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


class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'password')
    # list_filter = ('category', 'is_active')
    # search_fields = ('title', 'content')
    # list_editable = ('is_active',)

    def image_preview(self, obj):
        return obj.image.url if obj.image else None

    image_preview.short_description = 'Image Preview'
    image_preview.allow_tags = True


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Onbording, OnbordingAdmin)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(SelectCountry)
admin.site.register(Topics)
admin.site.register(NewsScoure)
