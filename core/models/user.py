from django.contrib.auth.models import AbstractUser
from django.db import models


class Skill(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


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
    skill = models.ManyToManyField(
        Skill, related_name='user_skill', blank=True, null=True
    )

    @property
    def get_full_name(self):
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        elif self.first_name and not self.last_name:
            return f"{self.first_name}"
        else:
            return self.username

    @property
    def get_path(self):
        if self.profile_picture and hasattr(self.profile_picture, 'url'):
            return self.profile_picture.url
        return '/static/images/avatar.png'
    
    @property
    def get_user_type(self):
        return dict(USER_TYPE_CHOICES).get(self.user_type, "Admin")