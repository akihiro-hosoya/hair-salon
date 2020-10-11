from django.db import models
from accounts.models import CustomUser
from django.utils import timezone

class User(models.Model):
    account_core = models.OneToOneField(CustomUser, verbose_name='アカウント', on_delete=models.CASCADE)
    furigana = models.CharField(('フリガナ'), max_length=50, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
    adress = models.CharField(('住所'), max_length=100, null=True, blank=True)
    description = models.TextField('備考欄', default="", blank=True)
    created = models.DateTimeField(('来店日'), default=timezone.now)

    def __str__(self):
        return self.account_core.name

class Staff(models.Model):
    account_core = models.OneToOneField(CustomUser, verbose_name='アカウント', on_delete=models.CASCADE)
    furigana = models.CharField(('フリガナ'), max_length=50, null=True, blank=True)
    position = models.CharField(('役職'), max_length=30, blank=True)
    description = models.TextField('自己紹介', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='プロフィール画像', null=True, blank=True)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
    adress = models.CharField(('住所'), max_length=100, null=True, blank=True)
    created = models.DateTimeField(('勤務開始日'), default=timezone.now)

    def __str__(self):
        return self.account_core.name