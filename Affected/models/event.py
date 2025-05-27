from django.db import models
from django.db.models import JSONField
from .relief import STATUS_CHOICES

EVENT_TYPE_CHOICES = [
    ('flood', 'Flood'),
    ('fire', 'Fire'),
    ('earthquake', 'Earthquake'),
    ('pandemic', 'Pandemic'),
]

INTENSITY_CHOICES = [
    ('low', 'Low'),
    ('medium', 'Medium'),
    ('high', 'High'),
]


class Event(models.Model):
    """Model representing an event that affects people."""
    user = models.ForeignKey(
        'core.User', on_delete=models.CASCADE, related_name='events', null=True
    )
    event_type = models.CharField(
        max_length=20, choices=EVENT_TYPE_CHOICES, default='flood'
    )
    specific_details = JSONField(null=True, blank=True)
    title = models.CharField(max_length=100)
    intensity = models.CharField(
        max_length=20, choices=INTENSITY_CHOICES, default='high'
    )
    color = models.CharField(max_length=7, default='#FF0000')
    description = models.TextField()
    date = models.DateTimeField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=255)
    radius = models.FloatField()
    affected_people = models.IntegerField()
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='open'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.intensity == 'low':
            self.color = '#81e008'
        elif self.intensity == 'medium':
            self.color = '#e0b208'
        elif self.intensity == 'high':
            self.color = '#FF0000'
        super().save(*args, **kwargs)


class AffectedPeopleImages(models.Model):
    """ Affected people images model """
    event_type = models.CharField(
        max_length=20, choices=EVENT_TYPE_CHOICES, default='flood'
    )
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='affected_people_images/')
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
