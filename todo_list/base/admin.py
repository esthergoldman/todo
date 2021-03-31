from django.contrib import admin
from .models import Task

# class BaseAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'title','')
#     list_display_links = ('id', 'title', 'user')
    

admin.site.register(Task)