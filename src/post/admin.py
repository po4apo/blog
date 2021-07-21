from django.contrib import admin
from django.utils.safestring import mark_safe

from post.models import Post, Category, Coment, Image


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'category')
    prepopulated_fields = {"slug": ("title",)}


class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'image', 'preview', 'image_img')

    readonly_fields = ["preview"]

    def preview(self, obj):
        return mark_safe(f'<img src="{obj.image.url}">')


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Coment)
admin.site.register(Image, ImageAdmin)
