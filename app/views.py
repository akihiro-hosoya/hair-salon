from django.views.generic import View, TemplateView
from django.shortcuts import render
from .models import User, Staff, News


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