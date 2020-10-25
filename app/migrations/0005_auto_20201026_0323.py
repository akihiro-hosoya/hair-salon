# Generated by Django 2.2.16 on 2020-10-25 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20201026_0224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='news', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='staff', verbose_name='プロフィール画像'),
        ),
        migrations.AlterField(
            model_name='style',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='style', verbose_name='画像'),
        ),
    ]
