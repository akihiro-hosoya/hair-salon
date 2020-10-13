from django.urls import path
from appointment import views

urlpatterns = [
    path('stylist/', views.StylistChoiceView.as_view(), name='stylist_choice'),
    path('calendar/<int:pk>/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/<int:pk>/<int:year>/<int:month>/<int:day>/', views.CalendarView.as_view(), name='calendar'),
    path('booking/<int:pk>/<int:year>/<int:month>/<int:day>/<int:hour>/', views.BookingView.as_view(), name='booking'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'),
    path('stylist_page/<int:year>/<int:month>/<int:day>/', views.StylistPageView.as_view(), name='stylist_page'),
]