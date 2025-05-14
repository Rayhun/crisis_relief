from django.db import models
from django.db.models import JSONField
from .relief import STATUS_CHOICES

EVENT_TYPE_CHOICES = [
    ('flood', 'Flood'),
    ('fire', 'Fire'),
    ('earthquake', 'Earthquake'),
    ('pandemic', 'Pandemic'),
]


class Event(models.Model):
    """Model representing an event that affects people."""
    event_type = models.CharField(
        max_length=20, choices=EVENT_TYPE_CHOICES, default='flood'
    )
    specific_details = JSONField(null=True, blank=True)  # To store event-specific data
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=100)
    radius = models.FloatField()
    affected_people = models.IntegerField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='open'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
