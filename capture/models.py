from django.db import models

# Create your models here.

class Capture(models.Model):

    imglink = models.CharField(max_length=1024)

    def __str__(self):
        return self.imglink

class Export(models.Model):

    src = models.CharField(max_length=1024)

    def __str__(self):
        return self.src