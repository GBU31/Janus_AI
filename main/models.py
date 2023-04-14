from django.db import models

class FileModel(models.Model):
    image = models.ImageField(upload_to='images/')
    video = models.FileField(upload_to='videos/')
