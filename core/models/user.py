from django.contrib.auth.models import AbstractUser
from django.db import models


USER_TYPE_CHOICES = (
        ('org', 'Organization'),
        ('volunteers', 'Volunteers'),
        ('donors', 'Donors'),
        ('affected', 'Affected'),
    )


class User(AbstractUser):
    user_type = models.CharField(max_length=10, choices=USER_TYPE_CHOICES)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True, null=True)
    address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=15, blank=True)
    profile_picture = models.ImageField(
        upload_to='profile_pics/', blank=True, null=True
    )
