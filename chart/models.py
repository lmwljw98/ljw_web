from django.db import models

# Create your models here.

class Rank(models.Model):

    naver_rank = models.CharField(max_length=1024, default=" ")

    daum_rank = models.CharField(max_length=1024, default=" ")

    melon_rank = models.CharField(max_length=1024, default=" ")

    def __str__(self):
        return self.naver_rank

    def __str__(self):
        return self.daum_rank

    def __str__(self):
        return self.melon_rank
