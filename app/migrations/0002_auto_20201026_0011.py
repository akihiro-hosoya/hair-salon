# Generated by Django 2.2.16 on 2020-10-25 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='画像'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='プロフィール画像'),
        ),
        migrations.AlterField(
            model_name='style',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/', verbose_name='画像'),
        ),
    ]