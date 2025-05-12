from django.db import models
from core.models import User


CATEGORY_CHOICES = [
    ('food', 'Food'),
    ('shelter', 'Shelter'),
    ('medical', 'Medical Supplies'),
    ('water', 'Clean Water'),
    ('other', 'Other'),
]


STATUS_CHOICES = [
    ('open', 'Open'),
    ('closed', 'Closed'),
    ('in_progress', 'In Progress'),
]


class ReliefRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(
        'Event', on_delete=models.CASCADE, related_name='relief_requests'
    )
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=100)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='open'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
