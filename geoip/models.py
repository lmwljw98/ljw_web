from django.db import models

# Create your models here.

class Input(models.Model):
    input = models.CharField(max_length=1024, null=True)

    def __str__(self):
        return self.input
