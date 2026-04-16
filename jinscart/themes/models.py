from django.db import models


class SiteSettings(models.Model):
    caption = models.CharField(max_length=255, default='JINSCART')
    banner_image_url = models.ImageField(upload_to='media/site_settings/', blank=True, null=True)


    def __str__(self):
        return self.caption
