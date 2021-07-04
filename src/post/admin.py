from django.contrib import admin

from post.models import Post, Category, Coment

class  PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'category')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
admin.site.register(Coment)
