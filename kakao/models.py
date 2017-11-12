from django.db import models

class UploadFileModel(models.Model):

    file = models.FileField(null=True)
