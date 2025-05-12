from django.db import models  

class Request(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('shelter', 'Shelter'),
        ('medical', 'Medical Supplies'),
        ('water', 'Clean Water'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Offer(models.Model):
    CATEGORY_CHOICES = [
        ('food', 'Food'),
        ('shelter', 'Shelter'),
        ('medical', 'Medical Supplies'),
        ('water', 'Clean Water'),
        ('other', 'Other'),
    ]

    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    location = models.CharField(max_length=100)
    status = models.CharField(max_length=20, default='Available')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
