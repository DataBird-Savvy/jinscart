from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    LIVE = 1
    DELETED = 0
    STATUS_CHOICES = (
        (LIVE, 'Live'),
        (DELETED, 'Deleted')
    )

    name = models.CharField(max_length=255)
    address = models.TextField(max_length=255)
    phone_number = models.CharField(max_length=20)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='customer_profile')
    deleted_status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
