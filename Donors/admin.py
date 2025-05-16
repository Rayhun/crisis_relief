from django.contrib import admin
from .models import Donation


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('id', 'donor', 'donation_type', 'amount', 'created_at')
    search_fields = ('user__username',)
    list_filter = ('donation_type',)
    ordering = ('-created_at',)

    def user(self, obj):
        return obj.user.username if obj.user else None
