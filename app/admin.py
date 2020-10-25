from django.contrib import admin
from .models import Gender, User, Staff, News, Style, StyleCategory, MenuCategory, Menu, Salon

# Register your models here.
admin.site.register(Gender)
admin.site.register(Salon)
admin.site.register(User)
admin.site.register(Staff)
admin.site.register(News)
admin.site.register(Style)
admin.site.register(StyleCategory)
admin.site.register(MenuCategory)
admin.site.register(Menu)