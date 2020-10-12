from django.shortcuts import get_object_or_404, render, redirect
from app.models import User, Staff
from .models import Stylist, Booking
from django.views.generic import View
from datetime import datetime, date, timedelta, time
from django.db.models import Q
from django.utils.timezone import localtime, make_aware
from .forms import BookingForm
from accounts.models import CustomUser

class StylistChoiceView(View):
    def get(self, request, *args, **kwargs):
        stylist_data = Stylist.objects.order_by('-id')

        return render(request, 'appointment/stylist_choice.html', {
            'stylist_data': stylist_data,
        })

class CalendarView(View):
    def get(self, request, *args, **kwargs):
        stylist_data = Stylist.objects.filter(id=self.kwargs['pk'])[0]
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
        booking_data = Booking.objects.filter(stylist=stylist_data).exclude(Q(start__gt=end_time) | Q(end__lt=start_time))
        for booking in booking_data:
            local_time = localtime(booking.start)
            booking_date = local_time.date()
            booking_hour = local_time.hour
            if (booking_hour in calendar) and (booking_date in calendar[booking_hour]):
                calendar[booking_hour][booking_date] = False

        return render(request, 'appointment/calendar.html', {
            'stylist_data': stylist_data,
            'calendar': calendar,
            'days': days,
            'start_day': start_day,
            'end_day': end_day,
            'before': days[0] - timedelta(days=7),
            'next': days[-1] + timedelta(days=1),
            'today': today,
        })

class BookingView(View):
    def get(self, request, *args, **kwargs):
        stylist_data = Stylist.objects.filter(id=self.kwargs['pk'])[0]
        user_data = User.objects.get(account_core_id=request.user.id)
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        hour = self.kwargs.get('hour')
        form = BookingForm(
            request.POST or None,
            initial={
                'name': user_data.account_core.name,
                'furigana': user_data.furigana,
                'address': user_data.address,
                'tel': user_data.tel,
            })

        return render(request, 'app/booking.html', {
            'stylist_data': stylist_data,
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'form': form,
        })

    def post(self, request, *args, **kwargs):
        stylist_data = get_object_or_404(Stylist, id=self.kwargs['pk'])
        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')
        hour = self.kwargs.get('hour')
        start_time = make_aware(datetime(year=year, month=month, day=day, hour=hour))
        end_time = make_aware(datetime(year=year, month=month, day=day, hour=hour + 1))
        booking_data = Booking.objects.filter(stylist=stylist_data, start=start_time)
        form = BookingForm(request.POST or None)
        if booking_data.exists():
            form.add_error(None, '既に予約があります。\n別の日時で予約をお願いします。')
        else:
            if form.is_valid():
                booking = Booking()
                booking.stylist = stylist_data
                booking.start = start_time
                booking.end = end_time
                booking.name = form.cleaned_data['name']
                booking.furigana = form.c_leaned_data['furigana']
                booking.tel = form.cleaned_data['tel']
                booking.address = form.cleaned_data['address']
                booking.remarks = form.cleaned_data['remarks']
                booking.save()
                return redirect('stylist_choice') # あとで変更

        return render(request, 'ec/booking.html', {
            'stylist_data': stylist_data,
            'year': year,
            'month': month,
            'day': day,
            'hour': hour,
            'form': form,
        })