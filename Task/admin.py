from django.contrib import admin
from .models import Task, Tag, TaskComment


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('ticket_id', 'title', 'status', 'user', 'priority', 'is_completed')
    list_filter = ('status', 'priority', 'user')
    search_fields = ('title', 'description')
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
    list_editable = ('is_completed',)
    prepopulated_fields = {'ticket_id': ('title',)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
    ordering = ('name',)


@admin.register(TaskComment)
class TaskCommentAdmin(admin.ModelAdmin):
    list_display = ('task', 'user', 'comment', 'created_at')
    list_filter = ('task', 'user')
    search_fields = ('comment',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
