from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
# Create your views here.
from .models import *
from .forms import *
from .filters import *


def home(request):
    orders = Order.objects.all()  # django shell function (API)???
    customers = Customer.objects.all()

    total_customers = customers.count()
    total_orders = orders.count()
    delivered = orders.filter(status = 'Delivered').count()
    pending = orders.filter(status = 'Pending').count()  # this status is the database columns
    context = {'orders': orders, 'customers': customers, 'total_customers': total_customers, 'total_orders':
        total_orders, 'delivered': delivered, 'pending': pending}
    # make a dictionary
    return render(request, 'accounts/dashboard.html', context)


def product(request):
    products = Product.objects.all()

    return render(request, 'accounts/product.html', {'products': products})  # we pass templates to products.html


def customer(request, pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    #when get request is received , the orders will be filtered to myFilter.qs

    myFilter = OrderFilter(request.GET, queryset = orders)
    orders = myFilter.qs

    context = {'customer': customer, 'orders': orders, 'order_count': order_count, 'myFilter':myFilter}
    return render(request, 'accounts/customer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields = ('product', 'status'), extra = 5)
    # fields is required coliums to be displayed
    customer = Customer.objects.get(id = pk)
    formset = OrderFormSet(queryset = Order.objects.none(), instance = customer)
    # form = OrderForm()
    if request.method == 'POST':
        # print('Printing POST:', request.POST)
        # form = OrderForm(request.POST)  # is a super handy way to do form saving
        formset = OrderFormSet(request.POST, instance = customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {'formset': formset}
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id = pk)
    form = OrderForm(instance = order)  # instance to indicate which order
    # start dicision making, when action='' redirect post to this url
    if request.method == 'POST':
        form = OrderForm(request.POST, instance = order)  # and save to that order
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id = pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
