from django.views.generic import View, TemplateView
from django.shortcuts import render
from .models import User, Staff, News, StyleCategory, Style, MenuCategory, Menu


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'app/index.html')

class AboutView(TemplateView):
    template_name = 'app/about.html'

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
        stylist_data = Staff.objects.order_by('id')

        return render(request, 'app/stylist_list.html', {
            'stylist_data': stylist_data,
        })

class StylistDetailView(View):
    def get(self, request, *args, **kwargs):
        stylist_data = Staff.objects.get(id=self.kwargs['pk'])        

        return render(request, 'app/stylist_detail.html', {
            'stylist_data': stylist_data,
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