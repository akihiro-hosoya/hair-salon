from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, ListView, DetailView, View
from .models import Item, OrderItem, Order, Payment
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from app.models import User, Staff
from accounts.models import CustomUser

# Create your views here.
class ItemListView(ListView):
    model = Item
    template_name = 'ec/item_list.html'

class ItemDetailView(DetailView):
    model = Item
    template_name = 'ec/item_detail.html'

@login_required
def addItem(request, slug):
    item = get_object_or_404(Item, slug=slug)
    user = User.objects.get(account_core_id=request.user.id)
    order_item, created = OrderItem.objects.get_or_create(
        item=item,
        user=user,
        ordered=False
    )
    order = Order.objects.filter(user=user, ordered=False)

    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item.quantity += 1
            order_item.save()
        else:
            order.items.add(order_item)
    else:
        order = Order.objects.create(user=user, ordered_date=timezone.now())
        order.items.add(order_item)

    return redirect('order')

class OrderView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(account_core_id=request.user.id)
        try:
            order = Order.objects.get(user=user, ordered=False)
            context = {
                'order': order
            }
            return render(request, 'ec/order.html', context)
        except ObjectDoesNotExist:
            return render(request, 'ec/order.html')

@login_required
def removeItem(request, slug):
    item = get_object_or_404(Item, slug=slug)
    user = User.objects.get(account_core_id=request.user.id)
    order = Order.objects.filter(
        user=user,
        ordered=False
    )
    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=user,
                ordered=False
            )[0]
            order.items.remove(order_item)
            order_item.delete()
            return redirect("order")

    return redirect("item_detail", slug=slug)

@login_required
def removeSingleItem(request, slug):
    item = get_object_or_404(Item, slug=slug)
    user = User.objects.get(account_core_id=request.user.id)
    order = Order.objects.filter(
        user=user,
        ordered=False
    )
    if order.exists():
        order = order[0]
        if order.items.filter(item__slug=item.slug).exists():
            order_item = OrderItem.objects.filter(
                item=item,
                user=user,
                ordered=False
            )[0]
            if order_item.quantity > 1:
                order_item.quantity -= 1
                order_item.save()
            else:
                order.items.remove(order_item)
                order_item.delete()
            return redirect("order")

    return redirect("item_detail", slug=slug)

class PaymentView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user = User.objects.get(account_core_id=request.user.id)
        order = Order.objects.get(user=user, ordered=False)
        user_data = User.objects.get(account_core_id=request.user.id)
        context = {
            'order': order,
            'user_data': user_data
        }
        return render(request, 'ec/payment.html', context)

    def post(self, request, *args, **kwargs):
        user = User.objects.get(account_core_id=request.user.id)
        order = Order.objects.get(user=user, ordered=False)
        order_items = order.items.all()
        amount = order.get_total()

        payment = Payment(user=user)
        payment.stripe_charge_id = 'test_stripe_charge_id'
        payment.amount = amount
        payment.save()

        order_items.update(ordered=True)
        for item in order_items:
            item.save()

        order.ordered = True
        order.payment = payment
        order.save()
        return redirect('thanks')

class ThanksView(LoginRequiredMixin, TemplateView):
    template_name = 'ec/thanks.html'
