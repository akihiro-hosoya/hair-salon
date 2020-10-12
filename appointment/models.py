from django.conf import settings
from django.db import models
from app.models import User, Staff

class Stylist(models.Model):
    stylist_staff = models.OneToOneField(Staff, verbose_name='スタイリスト', on_delete=models.CASCADE)

    def __str__(self):
        return self.stylist_staff.account_core.name