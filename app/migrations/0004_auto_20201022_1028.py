# Generated by Django 2.2.16 on 2020-10-22 01:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201022_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salon',
            name='concept1',
            field=models.TextField(blank=True, default='', verbose_name='コンセプト１'),
        ),
        migrations.AlterField(
            model_name='salon',
            name='concept2',
            field=models.TextField(blank=True, default='', verbose_name='コンセプト2'),
        ),
    ]