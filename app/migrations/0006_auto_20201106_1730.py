# Generated by Django 2.2.16 on 2020-11-06 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201026_0323'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='プロフィール画像'),
        ),
        migrations.AlterField(
            model_name='style',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images', verbose_name='画像'),
        ),
    ]
