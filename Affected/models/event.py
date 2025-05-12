from django.db import models
from .relief import STATUS_CHOICES


class Event(models.Model):
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
