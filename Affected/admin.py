from django.contrib import admin
from Affected.models import Event, ReliefRequest


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'date', 'location', 'status')
    search_fields = ('title', 'location')
    list_filter = ('status',)
    ordering = ('-date',)
    date_hierarchy = 'date'


@admin.register(ReliefRequest)
class ReliefRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'event', 'status', 'created_at')
    search_fields = ('event__title', 'requester__username')
    list_filter = ('status',)
    ordering = ('-created_at',)
    date_hierarchy = 'created_at'
