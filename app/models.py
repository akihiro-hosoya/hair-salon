from django.db import models
from accounts.models import CustomUser
from django.utils import timezone
from django.urls import reverse

GENDER_CHOICES = (
    (1, '指定なし'),
    (2, '男性'),
    (3, '女性'),
)
class User(models.Model):
    account_core = models.OneToOneField(CustomUser, verbose_name='アカウント', on_delete=models.CASCADE)
    name = models.CharField('名前', max_length=50)
    furigana = models.CharField(('フリガナ'), max_length=50, null=True, blank=True)
    gender = models.CharField('性別', max_length=2, default=1,choices=GENDER_CHOICES, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
    address = models.CharField(('住所'), max_length=100, null=True, blank=True)
    description = models.TextField('備考欄', default="", blank=True)
    created = models.DateTimeField(('来店日'), default=timezone.now)

    def __str__(self):
        return f'{self.furigana}___{self.account_core.email}'

class Staff(models.Model):
    account_core = models.OneToOneField(CustomUser, verbose_name='アカウント', on_delete=models.CASCADE)
    name = models.CharField('名前', max_length=50)
    furigana = models.CharField(('フリガナ'), max_length=50, null=True, blank=True)
    gender = models.CharField(max_length=2, default=1,choices=GENDER_CHOICES, null=True, blank=True)
    position = models.CharField(('役職'), max_length=30, blank=True)
    description = models.TextField('自己紹介', default="", blank=True)
    image = models.ImageField(upload_to='images', verbose_name='プロフィール画像', null=True, blank=True)
    tel = models.CharField('電話番号', max_length=100, null=True, blank=True)
    address = models.CharField(('住所'), max_length=100, null=True, blank=True)
    created = models.DateTimeField(('勤務開始日'), default=timezone.now)

    def __str__(self):
        return f'{self.furigana}___{self.account_core.email}'

# サロン
class Salon(models.Model):
    name = models.CharField('サロン名', max_length=30, null=True, blank=True)
    sub = models.CharField('サブタイトル', max_length=50, null=True, blank=True)
    concept1 = models.TextField('コンセプト１', default="", blank=True)
    concept2 = models.TextField('コンセプト2', default="", blank=True)
    mail = models.CharField('メールアドレス', max_length=200, null=True, blank=True)
    tel = models.CharField('電話番号', max_length=200, null=True, blank=True)
    opening = models.CharField('開店時間', max_length=30, null=True, blank=True)
    closed = models.CharField('閉店時間', max_length=30, null=True, blank=True)
    regular_holiday = models.CharField(('定休日'), max_length=100, null=True, blank=True)
    address = models.CharField(('住所'), max_length=100, null=True, blank=True)
    access = models.TextField('アクセス', default="", blank=True)
    twitter = models.CharField('twitter', max_length=100, null=True, blank=True)
    instagram = models.CharField('instagram', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name

# News
class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='images', verbose_name='画像', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title


# Style
class StyleCategory(models.Model):
    name = models.CharField('カテゴリ', max_length=50)

    def __str__(self):
        return self.name

class Style(models.Model):
    category = models.ForeignKey(StyleCategory, verbose_name='スタイルカテゴリ', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    detail = models.TextField()
    stylist = models.ForeignKey(Staff, verbose_name='スタイリスト', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images', verbose_name='画像', null=True, blank=True)

    def __str__(self):
        return self.name


# メニュー
class MenuCategory(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(MenuCategory, verbose_name='メニュカテゴリー', on_delete=models.CASCADE)
    description = models.TextField(default="", blank=True)
    time = models.IntegerField()

    def __str__(self):
        return self.title