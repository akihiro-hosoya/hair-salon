from django.conf import settings
from django.db import models
from app.models import User, Staff
from django.utils import timezone
from accounts.models import CustomUser

class Stylist(models.Model):
    detail = models.OneToOneField(Staff, verbose_name='スタイリスト', on_delete=models.CASCADE)

    def __str__(self):
        return self.detail.account_core.name

class Booking(models.Model):
    staff = models.ForeignKey(Staff, verbose_name='スタイリスト', on_delete=models.CASCADE)
    name = models.CharField('名前', max_length=50, null=True, blank=True)
    furigana = models.CharField('フリガナ', max_length=50, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=30, null=True, blank=True)
    remarks = models.TextField('備考', default="ご要望などをお書きください", blank=True)
    start = models.DateTimeField('開始時間', default=timezone.now)
    end = models.DateTimeField('終了時間', default=timezone.now)

    def __str__(self):
        start = timezone.localtime(self.start).strftime('%Y/%m/%d %H:%M')
        end = timezone.localtime(self.end).strftime('%Y/%m/%d %H:%M')
        return f'{self.name} {start} ~ {end} {self.staff}'