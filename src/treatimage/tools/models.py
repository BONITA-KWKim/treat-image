from django.db import models

# Create your models here.
class UploadImage(models.Model):
    raw_image = models.ImageField(upload_to='pic/',
                                  default='pic/None/no-img.jpg')
    created = models.DateTimeField(auto_now_add=True)

class ProcessedImage(models.Model):
    processed = models.ImageField(upload_to='processed_pic/',
                                  default='processed_pic/None/no-img.jpg')
    created = models.DateTimeField(auto_now_add=True)
