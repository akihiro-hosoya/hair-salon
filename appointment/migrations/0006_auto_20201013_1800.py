# Generated by Django 2.2.16 on 2020-10-13 09:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_auto_20201013_1753'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='stylist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Staff', verbose_name='スタイリスト'),
        ),
    ]