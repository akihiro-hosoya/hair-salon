# Generated by Django 2.2.16 on 2020-10-13 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0003_remove_booking_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stylist',
            old_name='stylist_staff',
            new_name='stylist',
        ),
    ]