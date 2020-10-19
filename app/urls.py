from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    # About
    path('about/', views.AboutView.as_view(), name='about'),
    # News
    path('news/', views.NewsListView.as_view(), name='news_list'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news_detail'),
    # Stylist
    path('stylists/', views.StylistListView.as_view(), name='stylist_list'),
    path('stylist/<int:pk>/', views.StylistDetailView.as_view(), name='stylist_detail'),
    # Style
    path('style/', views.StyleListView.as_view(), name='style_list'),
    path('style/<int:pk>/', views.StyleDetailView.as_view(), name='style_detail'),
    # Menu
    path('menu/', views.MenuView.as_view(), name='menu'),
    # Contact
    path('contact/', views.ContactView.as_view(), name='contact'),
    path('contact/thanks/', views.ContactThanksView.as_view(), name='contact_thanks'),
]