# Generated by Django 2.2.16 on 2020-10-18 12:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='画像')),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mail', models.CharField(blank=True, max_length=200, null=True, verbose_name='メールアドレス')),
                ('tel', models.CharField(blank=True, max_length=200, null=True, verbose_name='電話番号')),
                ('opening', models.CharField(blank=True, max_length=30, null=True, verbose_name='開店時間')),
                ('closed', models.CharField(blank=True, max_length=30, null=True, verbose_name='閉店時間')),
                ('regular_holiday', models.CharField(blank=True, max_length=100, null=True, verbose_name='定休日')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='住所')),
                ('access', models.TextField(blank=True, default='', verbose_name='アクセス')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名前')),
                ('furigana', models.CharField(blank=True, max_length=50, null=True, verbose_name='フリガナ')),
                ('gender', models.CharField(choices=[(1, '指定なし'), (2, '男性'), (3, '女性')], default=1, max_length=2)),
                ('position', models.CharField(blank=True, max_length=30, verbose_name='役職')),
                ('description', models.TextField(blank=True, default='', verbose_name='自己紹介')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='プロフィール画像')),
                ('tel', models.CharField(blank=True, max_length=100, null=True, verbose_name='電話番号')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='住所')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='勤務開始日')),
                ('account_core', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='アカウント')),
            ],
        ),
        migrations.CreateModel(
            name='StyleCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='カテゴリ')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='名前')),
                ('furigana', models.CharField(blank=True, max_length=50, null=True, verbose_name='フリガナ')),
                ('gender', models.CharField(choices=[(1, '指定なし'), (2, '男性'), (3, '女性')], default=1, max_length=2)),
                ('tel', models.CharField(blank=True, max_length=100, null=True, verbose_name='電話番号')),
                ('address', models.CharField(blank=True, max_length=100, null=True, verbose_name='住所')),
                ('description', models.TextField(blank=True, default='', verbose_name='備考欄')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='来店日')),
                ('account_core', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='アカウント')),
            ],
        ),
        migrations.CreateModel(
            name='Style',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('detail', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images', verbose_name='画像')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.StyleCategory', verbose_name='スタイルカテゴリ')),
                ('stylist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Staff', verbose_name='スタイリスト')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, default='')),
                ('time', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.MenuCategory', verbose_name='メニュカテゴリー')),
            ],
        ),
    ]
