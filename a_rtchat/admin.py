from django.contrib import admin

# Register your models here.

from .models import *

@admin.register(ChatGroup)
class ChatGroupAdmin(admin.ModelAdmin):
    list_display = ['group_name']

@admin.register(GroupMessage)
class GroupMessageAdmin(admin.ModelAdmin):
    list_display = ['group','author','body','created_at']
    list_filter = ['group','author']
    search_fields = ['group','author','body']
    date_hierarchy = 'created_at'