from django.db import models

class FileModel(models.Model):
    image_one = models.ImageField(upload_to='images/')
    image_two = models.ImageField(upload_to='images_two/')
