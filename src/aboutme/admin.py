from django.contrib import admin
from aboutme.models import Info

class ImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'name','photo', 'date', 'vk', 'email', 'number', 'github', 'skills', 'about_me', 'education')

admin.site.register(Info)

# Register your models here.
