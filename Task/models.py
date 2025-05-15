from django.db import models
from core.models import User
from Affected.models.event import STATUS_CHOICES


class Tag(models.Model):
    """
    Model representing a tag.
    """
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Task(models.Model):
    """
    Model representing a task.
    """
    PRIORITY_CHOICES = [
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
        ('urgent', 'Urgent'),
    ]
    ticket_id = models.CharField(max_length=255, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField(null=True, blank=True)
    priority = models.CharField(
        max_length=10, choices=PRIORITY_CHOICES, default='medium'
    )
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default='pending'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks'
    )
    tags = models.ManyToManyField('Tag', blank=True, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.ticket_id:
            super().save(*args, **kwargs)  # First save to generate pk
            self.ticket_id = f"TASK-{self.pk}"
            kwargs['force_insert'] = False  # Prevent duplicate insert
            super().save(*args, **kwargs)  # Save again to update ticket_id
        else:
            super().save(*args, **kwargs)

    @property
    def get_priority_color(self):
        """
        Returns the color associated with the task's priority.
        """
        colors = {
            'low': 'card-info',
            'medium': 'card-warning',
            'high': 'card-danger',
            'urgent': 'card-danger',
        }
        return colors.get(self.priority, 'gray')


class TaskComment(models.Model):
    """
    Model representing a comment on a task.
    """
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='task_comments')
    comment = models.TextField()
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')  # for reply support
    created_at = models.DateTimeField(auto_now_add=True)
