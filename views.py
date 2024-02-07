from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import never_cache

from .forms import OrderForm
from .models import Order
from django.contrib.auth.decorators import login_required


@login_required(login_url='login_url')
def add_order(request):
    template_name = 'CRUD_APP/order.html'
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


@login_required(login_url='login_url')
@never_cache
def show_orders(request):
    template_name = 'CRUD_APP/all_order.html'
    data = Order.objects.all()
    context = {'orders': data}
    return render(request, template_name, context)


def update_order(request, pk):
    template_name = 'CRUD_APP/order.html'
    obj = Order.objects.get(id=pk)
    form = OrderForm(instance=obj)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)


def delete_order(request, pk):
    template_name = 'CRUD_APP/confirm.html'
    obj = Order.objects.get(id=pk)
    if request.method == 'GET':
        context = {'Order': obj}
        return render(request, template_name, context)
    obj.delete()
    return redirect('show_url')
