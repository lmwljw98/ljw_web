from django.db import models


# Create your models here.

class My(models.Model):
    image_name = models.CharField(max_length=9999, default="")


class Gmy(models.Model):
    gif_name = models.CharField(max_length=9999, default="")
