from django.db import models


# Create your models here.

class Lock(models.Model):

    lock = models.CharField(max_length=100, default="on")

    def __str__(self):
        return self.lock


TV_CHOICES = (
    ('produce101', '프로듀스 101'),
    ('behind', '프로듀스 101 비하인드'),
    ('standby', '스탠바이 아이오아이'),
    ('snl', 'SNL KOREA 시즌7'),
    ('taxi', '현장토크쇼 TAXI'),
    ('sin3', '신서유기3'),
    ('sin4', '신서유기4'),
    ('goblin', '도깨비'),
    ('food3_sea_1', '삼시세끼 어촌편 1'),
    ('food3_sea_2', '삼시세끼 어촌편 2'),
    ('high_rap', '고등래퍼'),
    ('life_', '인생술집'),
    ('genious_2', '더 지니어스2 - 룰 브레이커'),
    ('genious_3', '더 지니어스3 - 블랙 가넷'),
    ('genious_4', '더 지니어스4 - 그랜드 파이널'),
    ('yoon', '윤식당'),
    ('ddl', 'Dodaeng\'s Diary in LA'),
    ('rngownj', '구해줘'),
)

class Tv_choice(models.Model):

    tv = models.CharField(max_length=50, choices=TV_CHOICES, default='green')
    num = models.CharField(max_length=5, default='1', null=False)


    def __str__(self):
        return self.tv

    def __str__(self):
        return self.num


class Output(models.Model):
    src = models.CharField(max_length=1024)

    def __str__(self):
        return self.src
