# Generated by Django 2.2.16 on 2020-10-22 02:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201022_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.CharField(blank=True, choices=[(1, '指定なし'), (2, '男性'), (3, '女性')], default=1, max_length=2, null=True),
        ),
    ]
