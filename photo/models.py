from django.db import models

# Create your models here.

class Links(models.Model):

    img = models.CharField(max_length=1024)

    def __str__(self):
        return self.img

class Mydata(models.Model):

    code = models.CharField(max_length=50, default='kimsohye', null=False)
    page = models.CharField(max_length=10, default='1', null=False)

    def __str__(self):
        return self.code

    def __str__(self):
        return self.page