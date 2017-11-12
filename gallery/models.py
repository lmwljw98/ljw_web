from django.db import models

# Create your models here.

class Photo(models.Model):

    source = models.CharField(max_length=500, null=False)
    text = models.CharField(max_length=500, null=False)
    start = models.CharField(max_length=500, null=False, default='1')
    end = models.CharField(max_length=500, null=False, default='5')

    def __str__(self):
        return self.source

    def __str__(self):
        return self.text