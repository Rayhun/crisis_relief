from django.db import models
from core.models import User


class Donation(models.Model):
    DONATION_TYPE_CHOICES = [
        ('money', 'Money'),
        ('goods', 'Goods'),
    ]

    LOGISTICS_TYPE_CHOICES = [
        ('pickup', 'Pickup from donor'),
        ('delivery', 'Donor will deliver'),
    ]

    donor = models.ForeignKey(User, on_delete=models.CASCADE)
    donation_type = models.CharField(
        max_length=10, choices=DONATION_TYPE_CHOICES, null=True,
    )
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True
    )  # for money
    item_description = models.TextField(null=True, blank=True)  # for goods
    quantity = models.PositiveIntegerField(null=True, blank=True)
    logistics_type = models.CharField(
        max_length=10, choices=LOGISTICS_TYPE_CHOICES, null=True, blank=True
    )
    pickup_latitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    pickup_longitude = models.DecimalField(
        max_digits=9, decimal_places=6, null=True, blank=True
    )
    pickup_address = models.TextField(null=True, blank=True)
    delivery_time = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.donor.username} - {self.donation_type}"
