from django.db import models

class Product(models.Model):

    LIVE = 1
    DELETED = 0
    STATUS_CHOICES = (
        (LIVE, 'Live'),
        (DELETED, 'Deleted')
    )
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image_url = models.ImageField(upload_to='media/products/')
    priority = models.IntegerField(default=0)
    deleted_status = models.IntegerField(choices=STATUS_CHOICES, default=LIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

