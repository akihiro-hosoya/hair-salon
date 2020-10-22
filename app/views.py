from django.views.generic import View, TemplateView
from django.shortcuts import render, redirect
from .models import User, Staff, News, StyleCategory, Style, MenuCategory, Menu, Salon
from appointment.models import Stylist, Booking
from django.utils.timezone import localtime, make_aware
from datetime import datetime, date, timedelta, time
from django.db.models import Q
from .forms import ContactForm
from django.conf import settings
from django.core.mail import BadHeaderError, EmailMessage
from django.http import HttpResponse
import textwrap


class IndexView(View):
    def get(self, request, *args, **kwargs):
        news_data = News.objects.order_by('-id')[0:3]
        staff_data = Staff.objects.order_by('id')
        salon_data = Salon.objects.all()

        return render(request, 'app/index.html', {
            'news_data': news_data,
            'staff_data': staff_data,
            'salon_data': salon_data,
        })

class AboutView(View):
    def get(self, request, *args, **kwargs):
        salon_data = Salon.objects.filter()[0]

        return render(request, 'app/about.html', {
            'salon_data': salon_data,
        })

class NewsListView(View):
    def get(self, request, *args, **kwargs):
        news_data = News.objects.order_by('-id')

        return render(request, 'app/news_list.html', {
            'news_data': news_data,
        })

class NewsDetailView(View):
    def get(self, request, *args, **kwargs):
        news_data = News.objects.get(id=self.kwargs['pk'])

        return render(request, 'app/news_detail.html', {
            'news_data': news_data,
        })

class StylistListView(View):
    def get(self, request, *args, **kwargs):
        staff_data = Staff.objects.order_by('id')

        return render(request, 'app/stylist_list.html', {
            'staff_data': staff_data,
        })

class StylistDetailView(View):
    def get(self, request, *args, **kwargs):
        staff_data = Staff.objects.get(id=self.kwargs['pk'])

        today = date.today()
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        if year and month and day:
            # 週始め
            start_date = date(year=year, month=month, day=day)
        else:
            start_date = today
        # 1週間
        days = [start_date]
        days = [start_date + timedelta(days=day) for day in range(7)]
        start_day = days[0]
        end_day = days[-1]

        calendar = {}
        # 10時～20時
        for hour in range(10, 21):
            row = {}
            for day in days:
                row[day] = True
            calendar[hour] = row
        start_time = make_aware(datetime.combine(start_day, time(hour=10, minute=0, second=0)))
        end_time = make_aware(datetime.combine(end_day, time(hour=20, minute=0, second=0)))
        # 開始時間＜終了時間・終了時間＞開始時間
        booking_data = Booking.objects.filter(staff=staff_data).exclude(Q(start__gt=end_time) | Q(end__lt=start_time))
        for booking in booking_data:
            # 現地のタイムゾーンに変更
            local_time = localtime(booking.start)
            booking_date = local_time.date()
            booking_hour = local_time.hour
            if (booking_hour in calendar) and (booking_date in calendar[booking_hour]):
                calendar[booking_hour][booking_date] = False
        
        return render(request, 'app/stylist_detail.html', {
            'staff_data': staff_data,
            'calendar': calendar,
            'days': days,
            'start_day': start_day,
            'end_day': end_day,
            'before': days[0] - timedelta(days=7),
            'next': days[-1] + timedelta(days=1),
            'today': today,
        })

class StyleListView(View):
    def get(self, request, *args, **kwargs):
        style_category = StyleCategory.objects.all()
        style_data = Style.objects.order_by('id')

        return render(request, 'app/style_list.html', {
            'style_category': style_category,
            'style_data': style_data,
        })

class StyleDetailView(View):
    def get(self, request, *args, **kwargs):
        style_data = Style.objects.get(id=self.kwargs['pk'])

        return render(request, 'app/style_detail.html', {
            'style_data': style_data,
        })

class MenuView(View):
    def get(self, request, *args, **kwargs):
        menu_category = MenuCategory.objects.order_by('id')
        menu_data = Menu.objects.order_by('id')

        return render(request, 'app/menu.html', {
            'menu_data': menu_data,
            'menu_category': menu_category,
        })

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactForm(request.POST or None)

        return render(request, 'app/contact.html', {
            'form': form
        })
    
    def post(self, request, *args, **kwargs):
        form = form = ContactForm(
            request.POST or None,
            initial={
                'name': 山田太郎,
                'email': xxxxx@gmail.com,
                'message': お問い合わせ内容,
            })

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            subject = 'お問い合わせありがとうございます。'
            content = textwrap.dedent('''
                ※このメールはシステムからの自動返信です。
                
                {name} 様
                
                お問い合わせありがとうございました。
                以下の内容でお問い合わせを受け付けいたしました。
                内容を確認させていただき、ご返信させて頂きますので、少々お待ちください。
                
                --------------------
                ■お名前
                {name}
                
                ■メールアドレス
                {email}
                
                ■メッセージ
                {message}
                --------------------
                ''').format(
                    name=name,
                    email=email,
                    message=message
                )

            to_list = [email]
            bcc_list = [settings.EMAIL_HOST_USER]

            try:
                message = EmailMessage(subject=subject, body=content, to=to_list, bcc=bcc_list)
                message.send()
            except BadHeaderError:
                return HttpResponse("無効なヘッダが検出されました。")

            return redirect('contact_thanks')

        return render(request, 'app/contact.html', {
            'form': form
        })

class ContactThanksView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/thanks.html')
