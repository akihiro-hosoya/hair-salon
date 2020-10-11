from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, View
from .models import Item
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ItemListView(ListView):
    model = Item
    template_name = 'ec/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'ec/item_detail.html'